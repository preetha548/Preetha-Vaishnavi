// server.js

const express = require("express");
const app = express();

app.use(express.urlencoded({ extended: true }));

app.get("/", (req, res) => {

  res.send(`

  <!DOCTYPE html>
  <html>
  <head>
    <title>Refer a Friend Form</title>

    <style>

      body{
        background:#e8cfc9;
        font-family: Arial;
        padding:30px;
      }

      .container{
        width:700px;
        margin:auto;
      }

      h1{
        color:#1f5c66;
        font-size:50px;
        margin-bottom:40px;
      }
        

      label{
        display:block;
        font-size:20px;
        margin-top:25px;
        margin-bottom:10px;
        color:#333;
      }

      .row{
        display:flex;
        gap:20px;
      }

      input, textarea{
        width:100%;
        padding:18px;
        border:1px solid #3b6b72;
        background:#f4e9e7;
        font-size:18px;
        box-sizing:border-box;
      }

      textarea{
        height:120px;
        resize:none;
      }

      button{
        display:block;
        margin:40px auto;
        padding:18px 60px;
        border:none;
        border-radius:40px;
        background:#2f6770;
        color:white;
        font-size:24px;
        cursor:pointer;
      }

      button:hover{
        background:#234f56;
      }

    </style>

  </head>

  <body>

    <div class="container">

      <h1>Refer a Friend Form</h1>

      <form action="/submit" method="POST">

        <label>Your Name</label>

        <div class="row">
          <input type="text" name="yourFirst" placeholder="First">
          <input type="text" name="yourLast" placeholder="Last">
        </div>

        <label>Person you are referring</label>

        <div class="row">
          <input type="text" name="friendFirst" placeholder="First">
          <input type="text" name="friendLast" placeholder="Last">
        </div>

        <label>How do you know this person?</label>
        <textarea name="know"></textarea>

        <label>How long have you known this person?</label>
        <textarea name="long"></textarea>

        <label>Why do you think this person is a good fit with our team?</label>
        <textarea name="fit"></textarea>

        <label>Is there anything else we should know about this person?</label>
        <textarea name="more"></textarea>

        <label>Their Phone Number</label>
        <input type="text" name="phone" placeholder="### ### ####">

        <label>Their Email</label>
        <input type="email" name="email">

        <button type="submit">SEND</button>

      </form>

    </div>

  </body>
  </html>

  `);

});

app.post("/submit", (req, res) => {

  console.log(req.body);

  res.send(`

    <h1 style="text-align:center; font-family:Arial;">
      Form Submitted Successfully ✅
    </h1>

    <div style="text-align:center;">
      <a href="/">Go Back</a>
    </div>

  `);

});

app.listen(3000, () => {
  console.log("Server running on http://localhost:3000");
});