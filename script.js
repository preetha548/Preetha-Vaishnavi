document.getElementById("regForm").addEventListener("submit", function(e) {
  e.preventDefault();

  let childName = document.getElementById("childName").value;
  let parentName = document.getElementById("parentName").value;
  let email = document.getElementById("email").value;

  if (childName === "" || parentName === "" || email === "") {
    alert("Please fill all required fields!");
    return;
  }

  document.getElementById("message").innerText = "Form submitted successfully!";
  
  document.getElementById("regForm").reset();
});