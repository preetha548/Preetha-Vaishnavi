function showMessage() {
  alert("Welcome to Vetri Builders! Let's build your dream.");
}

function submitForm() {
  let name = document.getElementById("name").value;
  let response = document.getElementById("response");

  response.innerText = "Thank you " + name + "! We will contact you soon.";
  return false; // prevent page reload
}