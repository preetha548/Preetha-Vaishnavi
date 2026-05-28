// server.js

const express = require("express");
const app = express();

app.use(express.static("public"));

app.get("/", (req, res) => {
  res.send(`

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Pinterest Clone</title>

  <style>

    *{
      margin:0;
      padding:0;
      box-sizing:border-box;
      font-family:Arial, Helvetica, sans-serif;
    }

    body{
      background:#f5f5f5;
    }

    /* NAVBAR */

    .navbar{
      width:100%;
      height:80px;
      background:white;
      display:flex;
      align-items:center;
      justify-content:space-between;
      padding:0 25px;
      position:sticky;
      top:0;
      box-shadow:0 2px 10px rgba(0,0,0,0.05);
    }

    .left-nav{
      display:flex;
      align-items:center;
      gap:20px;
    }

    .logo{
      color:#e60023;
      font-size:32px;
      font-weight:bold;
    }

    .explore{
      font-size:18px;
      cursor:pointer;
    }

    .search-box{
      flex:1;
      margin:0 30px;
    }

    .search-box input{
      width:100%;
      padding:15px 20px;
      border:none;
      outline:none;
      border-radius:30px;
      background:#efefef;
      font-size:16px;
    }

    .right-nav{
      display:flex;
      gap:15px;
    }

    .login-btn{
      padding:12px 20px;
      border:none;
      border-radius:25px;
      background:white;
      font-weight:bold;
      cursor:pointer;
    }

    .signup-btn{
      padding:12px 20px;
      border:none;
      border-radius:25px;
      background:#e60023;
      color:white;
      font-weight:bold;
      cursor:pointer;
    }

    /* PROFILE */

    .profile{
      padding:50px 70px;
    }

    .profile h1{
      font-size:60px;
      margin-bottom:10px;
    }

    .profile-info{
      display:flex;
      align-items:center;
      gap:15px;
      margin-top:20px;
    }

    .circle{
      width:45px;
      height:45px;
      background:#ddd;
      border-radius:50%;
      display:flex;
      align-items:center;
      justify-content:center;
      font-weight:bold;
    }

    /* PINS */

    .pins{
      padding:20px 70px;
      display:grid;
      grid-template-columns:repeat(auto-fill,minmax(250px,1fr));
      gap:25px;
    }

    .pin{
      background:white;
      border-radius:20px;
      overflow:hidden;
      position:relative;
      transition:0.3s;
      cursor:pointer;
    }

    .pin:hover{
      transform:scale(1.03);
    }

    .pin img{
      width:100%;
      height:350px;
      object-fit:cover;
      display:block;
    }

    .menu{
      position:absolute;
      bottom:20px;
      left:20px;
      background:white;
      border-radius:15px;
      padding:10px;
      width:200px;
      box-shadow:0 5px 15px rgba(0,0,0,0.2);
    }

    .menu p{
      padding:12px;
      border-radius:10px;
      transition:0.3s;
    }

    .menu p:hover{
      background:#f2f2f2;
    }

    .more{
      padding:20px 70px;
      font-size:45px;
      font-weight:bold;
    }

    @media(max-width:768px){

      .navbar{
        flex-wrap:wrap;
        height:auto;
        padding:15px;
      }

      .search-box{
        width:100%;
        margin:15px 0;
      }

      .profile{
        padding:30px;
      }

      .profile h1{
        font-size:40px;
      }

      .pins{
        padding:20px;
      }

      .more{
        padding:20px;
        font-size:35px;
      }
    }

  </style>
</head>

<body>

  <!-- NAVBAR -->

  <div class="navbar">

    <div class="left-nav">
      <div class="logo">Pinterest</div>
      <div class="explore">Explore</div>
    </div>

    <div class="search-box">
      <input type="text" placeholder="Search for vegan dinner recipes">
    </div>

    <div class="right-nav">
      <button class="login-btn">Log in</button>
      <button class="signup-btn">Sign up</button>
    </div>

  </div>

  <!-- PROFILE -->

  <div class="profile">
    <h1>Profile</h1>
    <p>1 Pin · 3m</p>

    <div class="profile-info">
      <div class="circle">P</div>
      <h2>By preetha vaishnavi</h2>
    </div>
  </div>

  <!-- PINS -->

  <div class="pins">

    <div class="pin">

      <img src="https://images.unsplash.com/photo-1544025162-d76694265947?q=80&w=800&auto=format&fit=crop">

      <div class="menu">
        <p>Save image</p>
        <p>Download image</p>
        <p>Open link in new tab</p>
        <p>Report Pin for India law</p>
      </div>

    </div>

  </div>

  <div class="more">
    More like this
  </div>

</body>
</html>

  `);
});

app.listen(3000, () => {
  console.log("Server running on http://localhost:3000");
});