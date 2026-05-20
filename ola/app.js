

const express = require("express");

const app = express();
const PORT = 3000;

app.get("/", (req, res) => {
  res.send(`
  <!DOCTYPE html>
  <html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    <title>OLA Scooter</title>

    <style>
      *{
        margin:0;
        padding:0;
        box-sizing:border-box;
        font-family:Arial, sans-serif;
      }

      body{
        overflow:hidden;
        background:black;
      }

      .container{
        width:100%;
        height:100vh;
        position:relative;
        background:linear-gradient(to bottom,#001122,#03243f,#0f6d43);
        display:flex;
        justify-content:center;
        align-items:center;
      }

      .neon{
        position:absolute;
        border:4px solid #c7ff00;
        box-shadow:
          0 0 20px #c7ff00,
          0 0 40px #c7ff00,
          0 0 60px #c7ff00;
        transform:rotate(-15deg);
      }

      .n1{
        width:700px;
        height:350px;
      }

      .n2{
        width:500px;
        height:250px;
      }

      .n3{
        width:300px;
        height:150px;
      }

      .text{
        position:absolute;
        top:40px;
        left:50px;
        color:white;
        z-index:2;
      }

      .text h1{
        font-size:55px;
        line-height:1.1;
        font-weight:300;
      }

      .logo{
        position:absolute;
        top:30px;
        right:50px;
        color:white;
        text-align:right;
        z-index:2;
      }

      .logo h1{
        font-size:60px;
      }

      .logo p{
        letter-spacing:2px;
      }

      .scooter{
        position:relative;
        width:700px;
        height:320px;
        z-index:3;
      }

      /* Scooter Body */
      .body{
        position:absolute;
        width:420px;
        height:140px;
        background:black;
        border-radius:120px 120px 90px 90px;
        bottom:70px;
        left:150px;
        box-shadow:0 0 25px rgba(0,255,100,0.4);
      }

      /* Seat */
      .seat{
        position:absolute;
        width:150px;
        height:40px;
        background:#222;
        border-radius:30px;
        top:-20px;
        right:70px;
      }

      /* Front */
      .front{
        position:absolute;
        width:80px;
        height:190px;
        background:#111;
        left:120px;
        bottom:90px;
        border-radius:50px;
        transform:skewY(-10deg);
      }

      /* Handle */
      .handle{
        position:absolute;
        width:70px;
        height:12px;
        background:#111;
        top:-10px;
        left:20px;
        transform:rotate(-20deg);
        border-radius:10px;
      }

      /* Wheels */
      .wheel{
        position:absolute;
        width:110px;
        height:110px;
        border-radius:50%;
        background:#111;
        border:10px solid #222;
        bottom:0;
      }

      .wheel::after{
        content:"";
        position:absolute;
        width:40px;
        height:40px;
        background:#44ff00;
        border-radius:50%;
        top:25px;
        left:25px;
      }

      .wheel1{
        left:120px;
      }

      .wheel2{
        right:70px;
      }

      /* Circle */
      .circle{
        position:absolute;
        left:40px;
        bottom:80px;
        width:300px;
        height:300px;
        border-radius:50%;
        border:3px solid rgba(255,255,255,0.5);
        background:#01294f;
        z-index:4;
        overflow:hidden;
        box-shadow:0 0 20px rgba(255,255,255,0.4);
      }

      /* Handle image style using CSS */
      .mini-handle{
        position:absolute;
        width:150px;
        height:20px;
        background:#111;
        top:110px;
        left:70px;
        transform:rotate(-20deg);
        border-radius:10px;
      }

      .mini-stick{
        position:absolute;
        width:25px;
        height:120px;
        background:#111;
        left:95px;
        top:100px;
        border-radius:20px;
      }

      .mini-buttons{
        position:absolute;
        width:70px;
        height:90px;
        background:#222;
        border-radius:20px;
        left:80px;
        top:140px;
      }

      .mini-buttons::before{
        content:"";
        position:absolute;
        width:40px;
        height:40px;
        border-radius:50%;
        border:3px solid #555;
        top:20px;
        left:12px;
      }

      .circle-text{
        position:absolute;
        left:70px;
        bottom:340px;
        color:white;
        z-index:5;
        font-size:28px;
      }

      @media(max-width:900px){

        .text h1{
          font-size:30px;
        }

        .scooter{
          transform:scale(0.8);
        }

        .circle{
          width:200px;
          height:200px;
        }

        .circle-text{
          font-size:18px;
          bottom:230px;
        }
      }

    </style>
  </head>

  <body>

    <div class="container">

      <div class="neon n1"></div>
      <div class="neon n2"></div>
      <div class="neon n3"></div>

      <div class="text">
        <h1>
          THE FUTURE IS TOO <br>
          QUICK FOR THE PAST <br>
          TO CATCH UP.
        </h1>
      </div>

      <div class="logo">
        <h1>OLA</h1>
        <p>HELLO FUTURE!</p>
      </div>

      <div class="circle-text">
        OLA Scooters <br>
        Go from 0 to 40 <br>
        in 3.9 seconds
      </div>

      <div class="circle">
        <div class="mini-handle"></div>
        <div class="mini-stick"></div>
        <div class="mini-buttons"></div>
      </div>

      <div class="scooter">

        <div class="front">
          <div class="handle"></div>
        </div>

        <div class="body">
          <div class="seat"></div>
        </div>

        <div class="wheel wheel1"></div>
        <div class="wheel wheel2"></div>

      </div>

    </div>

  </body>
  </html>
  `);
});

app.listen(PORT, () => {
  console.log("Server running at http://localhost:3000");
});