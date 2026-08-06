const express = require("express");

const app = express();

const PORT = 3000;

app.use(express.urlencoded({extended:true}));


let courses=[
{
name:"Argentine Tango",
desc:"Traditional romantic tango style",
fee:"₹6000"
},
{
name:"Wedding Tango",
desc:"Special couple choreography",
fee:"₹10000"
},
{
name:"Stage Performance",
desc:"Professional dance training",
fee:"₹15000"
}
];


let trainers=[
"Sofia - Tango Champion",
"Carlos - Latin Dance Expert",
"Maria - Professional Trainer"
];


let bookings=[];



app.get("/",(req,res)=>{


let courseData=courses.map(c=>`

<div class="card">

<h2>${c.name}</h2>

<p>${c.desc}</p>

<h3>${c.fee}</h3>

<button onclick="book('${c.name}')">
Book Now
</button>

</div>

`).join("");



let trainerData=trainers.map(t=>`

<div class="trainer">

<h2>${t}</h2>

<p>
Dance Master
</p>

</div>

`).join("");



res.send(`

<!DOCTYPE html>

<html>

<head>

<title>Tango Dance Studio</title>


<style>


*{
margin:0;
padding:0;
box-sizing:border-box;
font-family:Poppins,Arial;
}


body{

background:#090014;

color:white;

}


/* Header */


header{

position:fixed;

width:100%;

top:0;

padding:20px 50px;

display:flex;

justify-content:space-between;

background:
linear-gradient(
90deg,
#12002b,
#000000,
#220011
);

z-index:100;

}


.logo{

font-size:35px;

font-weight:bold;

background:

linear-gradient(
45deg,
#ff004c,
#ffd700,
#8a2be2
);

-webkit-background-clip:text;

color:transparent;

}


nav a{

color:white;

text-decoration:none;

margin:15px;

font-size:18px;

}


nav a:hover{

color:#ffd700;

}




/* Hero */


.hero{

height:100vh;


background:

linear-gradient(
135deg,
rgba(255,0,76,.7),
rgba(0,0,255,.5),
rgba(255,215,0,.5)
),

url(
"https://images.unsplash.com/photo-1547153760-18fc86324498"
);


background-size:cover;

display:flex;

align-items:center;

justify-content:center;

text-align:center;

}



.hero h1{

font-size:80px;

text-shadow:

0 0 20px #ff004c;

}



.hero p{

font-size:25px;

margin:20px;

}




button{

padding:15px 35px;

border:none;

border-radius:50px;

font-size:18px;

cursor:pointer;


background:

linear-gradient(
45deg,
#ff004c,
#ffd700,
#8a2be2
);


color:white;


}




section{

padding:80px 50px;

}



.title{

text-align:center;

font-size:45px;

margin-bottom:40px;

background:

linear-gradient(
45deg,
#ffd700,
#ff004c,
#00ffff
);

-webkit-background-clip:text;

color:transparent;

}




.cards{


display:grid;

grid-template-columns:

repeat(auto-fit,minmax(250px,1fr));


gap:30px;


}



.card{


background:

linear-gradient(
135deg,
#1b0033,
#001f3f,
#330011
);


padding:35px;

border-radius:25px;


text-align:center;


border:

2px solid #ffd700;


transition:.5s;


}



.card:hover{


transform:

translateY(-15px);


box-shadow:

0 0 30px #ff004c;


}





.trainer{


padding:35px;

border-radius:25px;


text-align:center;


background:

linear-gradient(
45deg,
#4b0082,
#000080,
#8b0000
);


}





.gallery{


display:grid;

grid-template-columns:

repeat(auto-fit,minmax(250px,1fr));


gap:20px;


}



.gallery img{

width:100%;

height:250px;

object-fit:cover;

border-radius:25px;

border:

4px solid #ffd700;


}




input,textarea{


width:70%;

padding:15px;

margin:10px;

border-radius:15px;

border:none;


}




footer{


background:

linear-gradient(
90deg,
#ff004c,
#8a2be2,
#000080
);


padding:30px;

text-align:center;


}





</style>


</head>



<body>


<header>


<div class="logo">
Tango Fusion
</div>


<nav>

<a href="#">
Home
</a>

<a href="#course">
Courses
</a>

<a href="#trainer">
Trainers
</a>

<a href="#contact">
Contact
</a>


</nav>


</header>




<div class="hero">


<div>


<h1>
TANGO FUSION
</h1>


<p>
Passion • Rhythm • Love • Elegance
</p>


<button onclick="welcome()">
Start Dance
</button>


</div>


</div>






<section id="course">


<h1 class="title">
Dance Programs
</h1>


<div class="cards">

${courseData}

</div>


</section>






<section id="trainer">


<h1 class="title">
Our Trainers
</h1>


<div class="cards">

${trainerData}

</div>


</section>





<section>


<h1 class="title">
Dance Gallery
</h1>


<div class="gallery">


<img src="https://images.unsplash.com/photo-1506157786151-b8491531f063">


<img src="https://images.unsplash.com/photo-1516280440614-37939bbacd81">


<img src="https://images.unsplash.com/photo-1519741497674-611481863552">


</div>


</section>






<section id="contact">


<h1 class="title">
Register Now
</h1>



<center>

<form method="post" action="/book">


<input name="name" placeholder="Name">


<br>


<input name="course" placeholder="Course">


<br>


<textarea placeholder="Message"></textarea>


<br>


<button>
Submit
</button>


</form>


</center>


</section>




<footer>

<h2>
Tango Fusion Dance Academy
</h2>

<p>
© 2026 Premium Dance Studio
</p>

</footer>




<script>

function welcome(){

alert(
"Welcome To Tango Fusion Academy"
);

}


function book(x){

alert(
"You selected "+x
);

}

</script>


</body>

</html>


`);

});





app.post("/book",(req,res)=>{

bookings.push(req.body);


res.send(

`
<h1>
🎉 Booking Confirmed
</h1>

<a href="/">
Return Home
</a>
`

);

});



app.get("/admin",(req,res)=>{

res.json(bookings);

});




app.listen(PORT,()=>{

console.log(
"Running at http://localhost:3000"
);

});