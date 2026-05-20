// app.js
const express = require("express");
const app = express();

app.get("/", (req, res) => {
  res.send(`
  <!DOCTYPE html>
  <html>
  <head>
    <title>Monthly Family Budget</title>
    <style>
      body{
        font-family: Arial, sans-serif;
        background:#f4f4f4;
        display:flex;
        justify-content:center;
        padding:20px;
      }

      .budget{
        width:800px;
        background:white;
        padding:20px;
        border:2px solid #ccc;
      }

      h1{
        color:#666;
        font-size:32px;
        margin-bottom:20px;
      }

      table{
        width:100%;
        border-collapse:collapse;
        margin-bottom:20px;
      }

      th, td{
        border:1px solid #999;
        height:35px;
        text-align:center;
      }

      th{
        background:#d9f0f0;
        color:#007777;
      }

      .section-title{
        color:#007777;
        font-size:24px;
        margin:10px 0;
      }

      .green-row:nth-child(even){
        background:#eef7ea;
      }

      .totals{
        font-weight:bold;
        color:#007777;
      }
    </style>
  </head>

  <body>

    <div class="budget">
      <h1>Monthly Family Budget</h1>

      <div class="section-title">Income Sources</div>
      <table>
        <tr>
          <th>Source</th>
          <th>January</th>
          <th>February</th>
          <th>March</th>
          <th>April</th>
        </tr>

        <tr class="green-row"><td></td><td></td><td></td><td></td><td></td></tr>
        <tr class="green-row"><td></td><td></td><td></td><td></td><td></td></tr>
        <tr class="green-row"><td></td><td></td><td></td><td></td><td></td></tr>

        <tr class="totals">
          <td>Totals</td>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
        </tr>
      </table>

      <div class="section-title">Expenses</div>
      <table>
        <tr>
          <th>Expense</th>
          <th>January</th>
          <th>February</th>
          <th>March</th>
          <th>April</th>
        </tr>

        ${Array(15).fill(`
          <tr class="green-row">
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
          </tr>
        `).join("")}

        <tr class="totals">
          <td>Totals</td>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
        </tr>
      </table>

      <div class="section-title">Savings</div>
      <table>
        <tr>
          <th>Savings</th>
          <th>January</th>
          <th>February</th>
          <th>March</th>
          <th>April</th>
        </tr>

        <tr class="green-row"><td></td><td></td><td></td><td></td><td></td></tr>
        <tr class="green-row"><td></td><td></td><td></td><td></td><td></td></tr>
        <tr class="green-row"><td></td><td></td><td></td><td></td><td></td></tr>

        <tr class="totals">
          <td>Totals</td>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
        </tr>
      </table>

    </div>

  </body>
  </html>
  `);
});

app.listen(3000, () => {
  console.log("Server running at http://localhost:3000");
});