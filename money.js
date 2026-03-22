function showAmount() {
  let total = localStorage.getItem("total");
  alert(total);

  document.getElementById("value").innerHTML = total;
}

function withdraw(receipt) {
  let dailyWithdrawn = localStorage.getItem("dailyWithdrawn");
  let total = localStorage.getItem("total");
  let requested = parseFloat(document.getElementById("withdraw").value);
  let preDailyCal = parseFloat(dailyWithdrawn) + parseFloat(requested);
  alert(`pre ${preDailyCal}`);

  if (preDailyCal <= 250) {
    dailyWithdrawn = preDailyCal;
    total -= requested;
    localStorage.setItem("total", total);
    localStorage.setItem("dailyWithdrawn", dailyWithdrawn);
    if (receipt === true) {
      showReceipt(requested, total);
    }
  } else {
    alert(`You're over your amount`);
  }

  alert(total);
}

function showReceipt(taken, left) {
  document.getElementById("content").innerHTML = `Receipt
  £${taken} withdrawn
  £${left} remaining`;
}
function showAmount() {
  let total = localStorage.getItem("total");
  alert(total);

  document.getElementById("value").innerHTML = total;
}

function withdraw(receipt) {
  let dailyWithdrawn = localStorage.getItem("dailyWithdrawn");
  let total = localStorage.getItem("total");
  let requested = parseFloat(document.getElementById("withdraw").value);
  let preDailyCal = parseFloat(dailyWithdrawn) + parseFloat(requested);
  alert(`pre ${preDailyCal}`);

  if (preDailyCal <= 250) {
    dailyWithdrawn = preDailyCal;
    total -= requested;
    localStorage.setItem("total", total);
    localStorage.setItem("dailyWithdrawn", dailyWithdrawn);
    if (receipt === true) {
      showReceipt(requested, total);
    }
  } else {
    alert(`You're over your amount`);
  }

  alert(total);
}

function showReceipt(taken, left) {
  document.getElementById("content").innerHTML = `Receipt
  £${taken} withdrawn
  £${left} remaining`;
}
