document.getElementById("loanForm").addEventListener("submit", function(e) {
  e.preventDefault();

  const firstName = document.getElementById("firstName").value.trim();
  const lastName = document.getElementById("lastName").value.trim();
  const email = document.getElementById("email").value.trim();
  const mobile = document.getElementById("mobile").value.trim();
  const marital = document.querySelector('input[name="marital"]:checked');

  if (!firstName || !lastName || !email || !mobile) {
    alert("Please fill all required fields.");
    return;
  }

  if (!marital) {
    alert("Please select marital status.");
    return;
  }

  if (!validateEmail(email)) {
    alert("Invalid email.");
    return;
  }

  alert("Application submitted successfully!");
  this.reset();
});

function validateEmail(email) {
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
}