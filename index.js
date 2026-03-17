var inputText = document.querySelector("#txt-input");
var btn = document.querySelector("#btn");
var outputDiv = document.querySelector("#output");

function clickHandler() {
  var year = parseInt(inputText.value);

  if (isNaN(year)) {
    outputDiv.innerText = "Please enter a valid year";
    return;
  }

  if (year % 400 === 0) {
    outputDiv.innerText = year + " is a leap year";
  } 
  else if (year % 100 === 0) {
    outputDiv.innerText = year + " is not a leap year";
  } 
  else if (year % 4 === 0) {
    outputDiv.innerText = year + " is a leap year";
  } 
  else {
    outputDiv.innerText = year + " is not a leap year";
  }
}

btn.addEventListener("click", clickHandler);