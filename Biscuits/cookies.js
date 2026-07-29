var initialAccountIndex = -1;
var GSC_COOKIE = "gsc";

function getCookie(name) {
  // Since there are 2 gsc cookies (on specific domain (.mijn.ing.nl and .mijnzakelijk.ing.nl) and on
  // global domain (.ing.nl)), we have to remove the one on the global domain to prevent conflicts and
  // unpredictable behaviour. The for loop below will iterate through the array of cookies starting at 0.
  // Since the order of the cookies vary per browser, sometimes the wrong gsc cookie (on global domain)
  // is used for retrieving the value.
  document.cookie =
    "gsc=-1;expires=Thu, 01 Jan 1970 00:00:01 GMT;max-age=0;domain=.ing.nl;path=/";
  var cookies = document.cookie.split(";");
  var cookie = null;

  // Search for the desired cookie
  var len = cookies.length;
  for (var ix = 0; ix < len && cookie === null; ix++) {
    if (cookies[ix].trim().indexOf(name + "=") === 0) {
      cookie = decodeURIComponent(cookies[ix]).trim();
    }
  }

  return cookie;
}

function formatGSCCookie(value) {
  value = GSC_COOKIE + "=" + encodeURIComponent(value.substr(4));
  var optionsString = "";
  if (document.domain.indexOf("mijn.ing.nl") > -1) {
    optionsString += ";domain=mijn.ing.nl";
  }
  if (document.domain.indexOf("mijnzakelijk.ing.nl") > -1) {
    optionsString += ";domain=mijnzakelijk.ing.nl";
  }
  optionsString += ";path=/";

  return value + optionsString;
}

function determineInitialAccount(aiType, response) {
  var account = {};
  if (response !== undefined && response !== null) {
    var len = response.accounts.length;
    for (var ix = 0; ix < len; ix++) {
      if (ix === determineInitialAccountIndex(aiType, response)) {
        account = response.accounts[ix];
        account.index = ix;
      }
    }
  }
  return account;
}

function determineInitialAccountIndex(aiType, response) {
  // Determination of the initialAccountIndex is only done once
  initialAccountIndex = getAccountIndexFromGSCCookie(
    aiType,
    response.selectedPosition
  );
  if (initialAccountIndex > response.accounts.length - 1) {
    initialAccountIndex = 0;
  }

  return initialAccountIndex;
}

function addCookie(cookieName, cookieValue, path) {
  document.cookie = cookieName + "=" + cookieValue + ";path=" + path;
}

function removeCookie(cookieName, path) {
  document.cookie =
    cookieName +
    "=-1;expires=Thu, 01 Jan 1970 00:00:01 GMT;max-age=0;path=" +
    path;
}

function getAccountIndexFromGSCCookie(aiType, defaultAccountIndex) {
  var accountIndex = 0;
  var found;
  var gscCookie = getCookie(GSC_COOKIE);

  if (defaultAccountIndex !== undefined) {
    accountIndex = defaultAccountIndex;
  }

  if (gscCookie) {
    found = gscCookie.match(new RegExp("\\b" + aiType + "=([0-9]+)"));

    if (found !== null && found.length > 1) {
      accountIndex = parseInt(found[1]);
    }
  }

  return accountIndex;
}

function setAccountIndexInGSCCookie(aiType, accountIndex) {
  var cookieDefault = GSC_COOKIE + "=" + aiType + "=";
  var cookiePart = aiType + "=";
  var re1 = new RegExp("," + aiType + "=[^,]+");
  var re2 = new RegExp("=" + aiType + "=[^,]+");
  var gscCookie = getCookie(GSC_COOKIE);

  if (gscCookie === null) {
    gscCookie = cookieDefault + accountIndex;
  } else {
    switch (true) {
      case !re1.test(gscCookie) && !re2.test(gscCookie):
        gscCookie =
          gscCookie.length === 0
            ? cookieDefault + accountIndex
            : gscCookie + "," + cookiePart + accountIndex;
        break;
      default:
        gscCookie = gscCookie.replace(re1, "," + cookiePart + accountIndex);
        gscCookie = gscCookie.replace(re2, "=" + cookiePart + accountIndex);
    }
  }

  document.cookie = formatGSCCookie(gscCookie);
}
