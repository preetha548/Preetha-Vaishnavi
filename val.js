let attempts = 3;

function confirmDetails() {
  let acctNum = document.getElementById("acctNum").value;
  let pin = document.getElementById("pin").value;
  let correctAcct = "123";
  let correctPin = "123";

  if (acctNum === correctAcct && pin === correctPin && attempts > 0) {
    alert("Passed");
    window.location.replace("option.html");
    setAmount();
  } else if (attempts > 0) {
    attempts--;
    alert(`Sorry try again, you have ${attempts} remaining`);
  } else {
    alert(`You have ran out of attempts. Please seek a manager for
    assistance`);
  }
}

function run() {
  window.location.replace("option.html");
}
function helloWorld() {
  alert("Hello World");
}

function setAmount() {
  localStorage.setItem("total", 750);
  localStorage.setItem("dailyWithdrawn", 0);
}
