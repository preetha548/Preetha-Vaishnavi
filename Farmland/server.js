const express = require("express");

const app = express();

app.get("/", (req, res) => {
  res.send(`
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Farm House</title>

<style>

*{
    margin:0;
    padding:0;
    box-sizing:border-box;
    font-family:Arial,sans-serif;
}

body{
    background:#eef7ea;
}

/* HEADER */

header{
    background:green;
    color:white;
    padding:20px 50px;
    display:flex;
    justify-content:space-between;
    align-items:center;
}

header h1{
    font-size:35px;
}

nav a{
    color:white;
    text-decoration:none;
    margin-left:20px;
    font-size:18px;
    font-weight:bold;
}

/* HERO */

.hero{
    height:90vh;
    background-image:url('https://images.unsplash.com/photo-1506744038136-46273834b3fb');
    background-size:cover;
    background-position:center;
    display:flex;
    justify-content:center;
    align-items:center;
    flex-direction:column;
    text-align:center;
    color:white;
}

.hero h2{
    font-size:65px;
    text-shadow:2px 2px 5px black;
}

.hero p{
    font-size:25px;
    margin:20px 0;
}

.hero button{
    padding:15px 30px;
    border:none;
    border-radius:10px;
    background:orange;
    color:white;
    font-size:20px;
    cursor:pointer;
}

.hero button:hover{
    background:darkorange;
}

/* CARDS */

.cards{
    display:flex;
    justify-content:center;
    gap:30px;
    padding:60px 20px;
    flex-wrap:wrap;
}

.card{
    background:white;
    width:320px;
    border-radius:15px;
    overflow:hidden;
    box-shadow:0 5px 15px rgba(0,0,0,0.2);
    transition:0.3s;
}

.card:hover{
    transform:translateY(-10px);
}

.card img{
    width:100%;
    height:220px;
    object-fit:cover;
}

.card-content{
    padding:20px;
    text-align:center;
}

.card-content h3{
    color:green;
    margin-bottom:10px;
    font-size:28px;
}

.card-content p{
    font-size:18px;
}

/* GALLERY */

.gallery{
    padding:50px;
    text-align:center;
}

.gallery h2{
    color:green;
    font-size:45px;
    margin-bottom:30px;
}

.gallery-images{
    display:grid;
    grid-template-columns:repeat(auto-fit,minmax(250px,1fr));
    gap:20px;
}

.gallery-images img{
    width:100%;
    height:250px;
    object-fit:cover;
    border-radius:15px;
    transition:0.3s;
}

.gallery-images img:hover{
    transform:scale(1.05);
}

/* FOOTER */

footer{
    background:green;
    color:white;
    text-align:center;
    padding:20px;
    margin-top:40px;
}

/* RESPONSIVE */

@media(max-width:768px){

header{
    flex-direction:column;
}

nav{
    margin-top:15px;
}

.hero h2{
    font-size:40px;
}

.hero p{
    font-size:20px;
}

}

</style>
</head>

<body>

<header>

    <h1>🌾 Green Farm House</h1>

    <nav>
        <a href="#">Home</a>
        <a href="#">Farm</a>
        <a href="#">Gallery</a>
        <a href="#">Contact</a>
    </nav>

</header>

<section class="hero">

    <h2>Welcome To Farm House</h2>

    <p>Fresh Nature • Organic Farming • Happy Living</p>

    <button onclick="showMessage()">
        Explore Farm
    </button>

</section>

<section class="cards">

    <div class="card">

        <img src="https://images.unsplash.com/photo-1560493676-04071c5f467b">

        <div class="card-content">
            <h3>🏡 Farm House</h3>
            <p>Beautiful farmhouse with peaceful environment.</p>
        </div>

    </div>

    <div class="card">

        <img src="https://images.unsplash.com/photo-1501004318641-b39e6451bec6">

        <div class="card-content">
            <h3>🌱 Organic Crops</h3>
            <p>Natural farming with healthy organic vegetables.</p>
        </div>

    </div>

    <div class="card">

        <img src="https://images.unsplash.com/photo-1516467508483-a7212febe31a">

        <div class="card-content">
            <h3>🐄 Dairy Farm</h3>
            <p>Healthy cows producing fresh milk daily.</p>
        </div>

    </div>

</section>

<section class="gallery">

    <h2>Farm Gallery</h2>

    <div class="gallery-images">

        <img src="https://images.unsplash.com/photo-1506744038136-46273834b3fb">

        <img src="https://images.unsplash.com/photo-1464226184884-fa280b87c399">

        <img src="https://images.unsplash.com/photo-1499529112087-3cb3b73cec95">

        <img src="https://images.unsplash.com/photo-1500937386664-56d1dfef3854">

    </div>

</section>

<footer>

    <h2>© 2026 Green Farm House</h2>

</footer>

<script>

function showMessage(){
    alert("🌾 Welcome To Green Farm House 🌾");
}

</script>

</body>
</html>
  `);
});

app.listen(3000, () => {
  console.log("Server running on http://localhost:3000");
});