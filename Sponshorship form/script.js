function addRow() {
  const table = document.getElementById("tableBody");

  const row = document.createElement("tr");

  row.innerHTML = `
    <td><input type="text"></td>
    <td><input type="text"></td>
    <td><input type="text"></td>
    <td><input type="number"></td>
    <td><input type="checkbox"></td>
    <td><input type="checkbox"></td>
  `;

  table.appendChild(row);
}

// Add initial rows
for (let i = 0; i < 10; i++) {
  addRow();
}