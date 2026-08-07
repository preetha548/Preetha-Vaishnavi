const express = require("express");

const app = express();
const PORT = 3000;

app.get("/", (req, res) => {
    res.send(`
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Avocado Toast</title>

<style>
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: Georgia, "Times New Roman", serif;
    background: #ffffff;
    color: #111;
}

.container {
    width: 100%;
    max-width: 900px;
    margin: auto;
    background: white;
}

/* Main image */
.hero {
    width: 100%;
    overflow: hidden;
}

.hero img {
    width: 100%;
    display: block;
}

/* Title section */
.title {
    text-align: center;
    padding: 55px 20px;
    border-top: 3px solid #222;
    border-bottom: 3px solid #222;
    background: white;
}

.title h1 {
    font-size: 82px;
    font-weight: bold;
    line-height: 1.05;
    letter-spacing: 2px;
}

.title p {
    font-size: 68px;
    margin-top: 5px;
    font-weight: bold;
}

/* Bottom section */
.bottom {
    position: relative;
    overflow: hidden;
}

.bottom img {
    width: 100%;
    display: block;
}

/* Button-like labels */
.label {
    position: absolute;
    background: white;
    padding: 20px 28px;
    font-family: Arial, sans-serif;
    font-weight: bold;
    font-size: 25px;
    letter-spacing: 4px;
    text-align: center;
}

/* Responsive */
@media(max-width: 600px) {

    .title {
        padding: 30px 10px;
    }

    .title h1 {
        font-size: 45px;
    }

    .title p {
        font-size: 42px;
    }

    .label {
        font-size: 13px;
        padding: 10px;
        letter-spacing: 2px;
    }
}
</style>
</head>

<body>

<div class="container">

    <!-- Food Image -->
    <div class="hero">
        <img src="https://cdn.loveandlemons.com/wp-content/uploads/2019/12/avocado-toast-pin.jpg" alt="Avocado Toast">
    </div>

    <!-- Main Title -->
    <section class="title">
        <h1>Avocado</h1>
        <p>Toast</p>
    </section>

    <!-- Bottom Image -->
    <div class="bottom">
        <img src="/avocado-toast.png" alt="Avocado Toast">

        <div class="label" style="left:18%; top:20%;">
            TOAST-ADA<br>
            TOAST
        </div>

        <div class="label" style="right:18%; bottom:10%;">
            LOVE &amp; LEMONS
        </div>
    </div>

</div>

</body>
</html>
    `);
});

app.use(express.static("."));

app.listen(PORT, () => {
    console.log(`Server running at http://localhost:${PORT}`);
});