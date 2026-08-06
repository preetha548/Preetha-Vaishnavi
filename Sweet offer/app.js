const express = require("express");

const app = express();

app.get("/", (req, res) => {

res.send(`

<!DOCTYPE html>

<html>

<head>

<meta charset="UTF-8">

<title>Swiggy Banner</title>

<style>

*{
margin:0;
padding:0;
box-sizing:border-box;
font-family:Arial,Helvetica,sans-serif;
}

body{
background:#ffffff;
}

.banner{

width:100%;

height:420px;

background:#fde8de;

position:relative;

overflow:hidden;

display:flex;

justify-content:center;

align-items:center;
}

.banner::before{

content:'';

position:absolute;

width:1000px;

height:1000px;

border-radius:50%;

background:repeating-conic-gradient(

rgba(255,255,255,.4) 0deg,

rgba(255,255,255,.4) 12deg,

transparent 12deg,

transparent 24deg

);

opacity:.5;
}

.circle{

position:absolute;

width:250px;

height:250px;

border-radius:50%;

overflow:hidden;

border:8px solid #ffd4c1;

background:white;

box-shadow:0 10px 20px rgba(0,0,0,.2);

}

.circle img{

width:100%;

height:100%;

object-fit:cover;

}

.lt{

left:-50px;

top:-30px;
}

.lb{

left:-70px;

bottom:-60px;
}

.rt{

right:-60px;

top:-40px;
}

.rb{

right:-70px;

bottom:-60px;
}

.content{

position:relative;

z-index:100;

text-align:center;

width:500px;

}

.logo{

font-size:45px;

font-weight:bold;

color:#ff5200;

margin-bottom:20px;

}

.text{

font-size:34px;

font-weight:600;

line-height:1.4;

color:#222;

}

@media(max-width:900px){

.circle{

width:170px;

height:170px;

}

.text{

font-size:24px;

}

}

</style>

</head>

<body>

<div class="banner">

<div class="circle lt">
<img src="https://images.unsplash.com/photo-1519864600265-abb23847ef2c?w=500">
</div>

<div class="circle lb">
<img src="https://images.unsplash.com/photo-1606313564200-e75d5e30476c?w=500">
</div>

<div class="circle rt">
<img src="https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=500">
</div>

<div class="circle rb">
<img src="https://images.unsplash.com/photo-1563729784474-d77dbb933a9e?w=500">
</div>

<div class="content">

<div class="logo">
Swiggy
</div>

<div class="text">
Start the New Year on a sweet note with these delightful delicacies.
</div>

</div>

</div>

</body>

</html>

`);

});

app.listen(3000, () => {

console.log("Server Running");
console.log("http://localhost:3000");

});