// app.js
const express = require("express");
const app = express();

app.get("/", (req, res) => {
  res.send(`
  <!DOCTYPE html>
  <html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    <title>Feelings Chart</title>

    <style>
      *{
        margin:0;
        padding:0;
        box-sizing:border-box;
        font-family: Arial, sans-serif;
      }

      body{
        background:#efefef;
        padding:30px;
      }

      .title{
        width:100%;
        max-width:1100px;
        margin:auto;
        border:6px solid black;
        border-radius:40px;
        text-align:center;
        padding:25px;
        font-size:60px;
        font-weight:bold;
        letter-spacing:3px;
        background:white;
      }

      .days{
        display:grid;
        grid-template-columns: 220px repeat(7, 1fr);
        gap:18px;
        max-width:1100px;
        margin:40px auto 20px;
      }

      .day{
        background:#3daaf5;
        color:white;
        text-align:center;
        padding:14px;
        border-radius:20px;
        font-size:24px;
        font-weight:bold;
      }

      .empty{
        background:transparent;
      }

      .chart{
        max-width:1100px;
        margin:auto;
        display:flex;
        flex-direction:column;
        gap:18px;
      }

      .row{
        display:grid;
        grid-template-columns: 220px repeat(7, 1fr);
        gap:18px;
        align-items:center;
      }

      .emotion{
        color:white;
        font-size:22px;
        font-weight:bold;
        height:120px;
        display:flex;
        align-items:center;
        justify-content:center;
        border-radius:25px;
      }

      .box{
        height:120px;
        border:4px solid black;
        border-radius:25px;
        background:white;
        cursor:pointer;
        transition:0.3s;
      }

      .box:hover{
        background:#d9f0ff;
      }

      .active{
        background:#7dd3fc;
      }

      .red{
        background:#ff5b5b;
      }

      .pink{
        background:#ea5ab8;
      }

      .purple{
        background:#7b4df0;
      }

      .orange{
        background:#f59a12;
      }

      @media(max-width:900px){
        .title{
          font-size:35px;
        }

        .row,
        .days{
          grid-template-columns: 150px repeat(7, 90px);
          overflow-x:auto;
        }

        .emotion,
        .box{
          height:90px;
        }
      }
    </style>
  </head>

  <body>

    <div class="title">FEELINGS CHART</div>

    <div class="days">
      <div class="empty"></div>
      <div class="day">MON</div>
      <div class="day">TUE</div>
      <div class="day">WED</div>
      <div class="day">THU</div>
      <div class="day">FRI</div>
      <div class="day">SAT</div>
      <div class="day">SUN</div>
    </div>

    <div class="chart">

      <div class="row">
        <div class="emotion red">ANGER</div>
        <div class="box"></div><div class="box"></div><div class="box"></div>
        <div class="box"></div><div class="box"></div><div class="box"></div>
        <div class="box"></div>
      </div>

      <div class="row">
        <div class="emotion red">APATHY</div>
        <div class="box"></div><div class="box"></div><div class="box"></div>
        <div class="box"></div><div class="box"></div><div class="box"></div>
        <div class="box"></div>
      </div>

      <div class="row">
        <div class="emotion pink">FEAR</div>
        <div class="box"></div><div class="box"></div><div class="box"></div>
        <div class="box"></div><div class="box"></div><div class="box"></div>
        <div class="box"></div>
      </div>

      <div class="row">
        <div class="emotion pink">ANXIETY</div>
        <div class="box"></div><div class="box"></div><div class="box"></div>
        <div class="box"></div><div class="box"></div><div class="box"></div>
        <div class="box"></div>
      </div>

      <div class="row">
        <div class="emotion purple">SADNESS</div>
        <div class="box"></div><div class="box"></div><div class="box"></div>
        <div class="box"></div><div class="box"></div><div class="box"></div>
        <div class="box"></div>
      </div>

      <div class="row">
        <div class="emotion purple">GRIEF</div>
        <div class="box"></div><div class="box"></div><div class="box"></div>
        <div class="box"></div><div class="box"></div><div class="box"></div>
        <div class="box"></div>
      </div>

      <div class="row">
        <div class="emotion orange">HAPPINESS</div>
        <div class="box"></div><div class="box"></div><div class="box"></div>
        <div class="box"></div><div class="box"></div><div class="box"></div>
        <div class="box"></div>
      </div>

      <div class="row">
        <div class="emotion orange">JOY</div>
        <div class="box"></div><div class="box"></div><div class="box"></div>
        <div class="box"></div><div class="box"></div><div class="box"></div>
        <div class="box"></div>
      </div>

    </div>

    <script>
      const boxes = document.querySelectorAll(".box");

      boxes.forEach(box => {
        box.addEventListener("click", () => {
          box.classList.toggle("active");
        });
      });
    </script>

  </body>
  </html>
  `);
});

app.listen(3000, () => {
  console.log("Server running at http://localhost:3000");
});