const times = [
  "7:00 AM",
  "9:00 AM",
  "11:00 AM",
  "1:00 PM",
  "3:00 PM",
  "5:00 PM",
  "7:00 PM"
];

const tbody = document.getElementById("scheduleBody");

times.forEach(time => {

  const row = document.createElement("tr");

  row.innerHTML = `
    <td class="time">${time}</td>
    <td contenteditable="true"></td>
    <td contenteditable="true"></td>
    <td contenteditable="true"></td>
    <td contenteditable="true"></td>
    <td contenteditable="true"></td>
  `;

  tbody.appendChild(row);
});