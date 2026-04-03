let students = [];

// Navigation
function showSection(id) {
  document.querySelectorAll("#dashboard, #students, #attendance, #fees, #reports, #settings")
    .forEach(sec => sec.style.display = "none");

  document.getElementById(id).style.display = "block";
}

// Add student
function addStudent() {
  let name = document.getElementById("name").value;
  let marks = document.getElementById("marks").value;

  students.push({name, marks});
  displayStudents();
}

// Display
function displayStudents() {
  let table = document.getElementById("studentTable");
  table.innerHTML = "";

  students.forEach(s => {
    table.innerHTML += `<tr><td>${s.name}</td><td>${s.marks}</td></tr>`;
  });

  document.getElementById("totalStudents").innerText = students.length;
  document.getElementById("reportStudents").innerText = students.length;
}

// Search
function searchStudent() {
  let value = document.getElementById("search").value.toLowerCase();

  let rows = document.querySelectorAll("#studentTable tr");
  rows.forEach(row => {
    row.style.display = row.innerText.toLowerCase().includes(value) ? "" : "none";
  });
}

// Attendance
function markAttendance() {
  document.getElementById("attendanceStatus").innerText = "Marked Present ✔";
}

// Fees
function payFees() {
  let amt = document.getElementById("amount").value;
  document.getElementById("paymentStatus").innerText = "Paid ₹" + amt;
}

// Dark Mode
function darkMode() {
  document.body.classList.toggle("bg-dark");
  document.body.classList.toggle("text-white");
}

// Chart
const ctx = document.getElementById('chart');

new Chart(ctx, {
  type: 'bar',
  data: {
    labels: ['Math', 'Science', 'English'],
    datasets: [{
      label: 'Marks',
      data: [80, 70, 90],
      backgroundColor: ['blue','green','orange']
    }]
  }
});