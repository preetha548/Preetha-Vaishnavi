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

<title>Drink Prime - Pure Water</title>

<style>

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: Arial, Helvetica, sans-serif;
    background: #11141b;
    display: flex;
    justify-content: center;
    min-height: 100vh;
}

.ad-container {
    width: 430px;
    min-height: 100vh;
    background: linear-gradient(
        to bottom,
        #ffffff 0%,
        #f5f5f5 40%,
        #d7d7d7 55%,
        #3b3b3b 100%
    );
    overflow: hidden;
    position: relative;
}

/* LOGO */

.logo {
    position: absolute;
    right: 22px;
    top: 28px;
    text-align: center;
    color: #333;
    font-size: 11px;
    font-weight: bold;
}

.logo-symbol {
    color: #4039b9;
    font-size: 32px;
    font-weight: bold;
    line-height: 25px;
}

.logo span {
    display: block;
}

/* MAIN HEADING */

.heading {
    padding: 95px 15px 0;
    text-align: center;
}

.heading h1 {
    color: #4039bd;
    font-size: 43px;
    font-weight: 800;
    letter-spacing: -1px;
}

.heading p {
    font-size: 29px;
    margin-top: 5px;
    color: #111;
}

.heading p span {
    font-weight: bold;
}

/* OFFER */

.offer {
    margin: 30px auto 0;
    width: 80%;
    text-align: center;
    position: relative;
}

.offer-title {
    font-size: 18px;
    background: transparent;
    position: relative;
    z-index: 2;
}

.offer-title b {
    font-weight: 800;
}

.price {
    margin-top: 8px;
    background: #443cc0;
    color: white;
    padding: 10px;
    border-radius: 4px;
    font-size: 18px;
}

.price strong {
    font-size: 32px;
}

/* ZERO COST */

.zero-cost {
    display: flex;
    align-items: center;
    justify-content: center;
    margin-top: 28px;
    gap: 15px;
}

.zero {
    color: #4039bd;
    font-size: 105px;
    font-weight: 300;
    line-height: 90px;
}

.cost-list {
    font-size: 18px;
    font-weight: bold;
    line-height: 27px;
}

/* TRIAL BADGE */

.trial {
    position: absolute;
    top: 500px;
    left: 42px;
    width: 115px;
    height: 115px;
    border-radius: 50%;
    background: #4740c5;
    color: white;
    border: 5px solid #7770dc;
    box-shadow: 0 0 0 4px #fff;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    z-index: 5;
}

.trial .number {
    font-size: 40px;
    font-weight: bold;
}

.trial small {
    font-size: 12px;
}

.trial strong {
    font-size: 21px;
}

/* WATER EFFECT */

.water {
    position: absolute;
    top: 640px;
    left: 20px;
    right: 20px;
    height: 180px;
    background:
        radial-gradient(circle at 15% 50%, #ffffff 0 4px, transparent 5px),
        radial-gradient(circle at 85% 35%, #ffffff 0 3px, transparent 4px),
        radial-gradient(circle at 70% 75%, #ffffff 0 5px, transparent 6px);
    opacity: .8;
}

/* PURIFIER */

.purifier {
    position: relative;
    margin: 80px auto 0;
    width: 290px;
    height: 365px;
    background: linear-gradient(
        135deg,
        #ffffff,
        #e9e9e9
    );
    border-radius: 25px 25px 0 0;
    box-shadow: 0 8px 20px rgba(0,0,0,.2);
    overflow: visible;
}

.purifier::before {
    content: "";
    position: absolute;
    top: 0;
    right: 70px;
    width: 30px;
    height: 300px;
    background: #8d5c4b;
    border-radius: 0 0 20px 20px;
    transform: skew(-5deg);
}

.purifier::after {
    content: "";
    position: absolute;
    top: 0;
    right: 48px;
    width: 18px;
    height: 300px;
    background: #d8b49e;
    border-radius: 0 0 15px 15px;
    transform: skew(-5deg);
}

/* PURIFIER DISPLAY */

.display {
    position: absolute;
    top: 135px;
    left: 50%;
    transform: translateX(-50%);
    background: #111;
    width: 18px;
    height: 60px;
    border-radius: 5px;
    z-index: 3;
}

.display div {
    width: 7px;
    height: 7px;
    border: 1px solid white;
    border-radius: 50%;
    margin: 6px auto;
}

/* TAP */

.tap {
    position: absolute;
    bottom: 70px;
    left: 50%;
    transform: translateX(-50%);
    width: 32px;
    height: 45px;
    background: #111;
    border-radius: 5px;
    z-index: 3;
}

.tap::after {
    content: "";
    position: absolute;
    bottom: -18px;
    left: 10px;
    width: 12px;
    height: 20px;
    background: #111;
}

/* COPPER CIRCLES */

.copper {
    position: absolute;
    width: 35px;
    height: 35px;
    border-radius: 50%;
    background: radial-gradient(
        circle at 30% 30%,
        #ffe1ae,
        #a95617
    );
    color: white;
    font-size: 12px;
    font-weight: bold;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0 3px 7px #555;
    z-index: 4;
}

.c1 { left: -30px; top: 90px; }
.c2 { left: -10px; top: 190px; }
.c3 { right: -30px; top: 110px; }
.c4 { right: -10px; top: 230px; }
.c5 { left: 120px; bottom: 35px; }

/* PERSON */

.person {
    position: absolute;
    bottom: 0;
    right: -15px;
    width: 170px;
    height: 340px;
    z-index: 6;
}

.head {
    position: absolute;
    top: 5px;
    right: 20px;
    width: 105px;
    height: 120px;
    background: #b97854;
    border-radius: 48% 48% 45% 45%;
    z-index: 2;
}

.hair {
    position: absolute;
    top: -10px;
    right: 5px;
    width: 130px;
    height: 190px;
    background: #171313;
    border-radius: 60% 60% 40% 50%;
    z-index: 1;
}

.body {
    position: absolute;
    bottom: 0;
    right: 5px;
    width: 155px;
    height: 205px;
    background: #d9e2eb;
    border-radius: 70px 70px 0 0;
}

.shirt-line {
    position: absolute;
    top: 45px;
    left: 65px;
    width: 2px;
    height: 140px;
    background: #8995a3;
}

.arm {
    position: absolute;
    bottom: 35px;
    left: -35px;
    width: 100px;
    height: 35px;
    background: #b97854;
    border-radius: 30px;
    transform: rotate(-20deg);
}

.glass {
    position: absolute;
    bottom: 55px;
    left: -75px;
    width: 50px;
    height: 70px;
    border: 3px solid rgba(255,255,255,.8);
    background: rgba(255,255,255,.25);
    border-radius: 0 0 12px 12px;
    z-index: 10;
}

.glass::after {
    content: "";
    position: absolute;
    bottom: 0;
    left: 3px;
    width: 38px;
    height: 35px;
    background: rgba(100,180,255,.35);
}

/* SOCIAL AREA */

.social {
    position: absolute;
    right: 10px;
    bottom: 105px;
    color: white;
    text-align: center;
    z-index: 10;
}

.social div {
    margin: 15px 0;
    font-size: 25px;
}

.social small {
    display: block;
    font-size: 12px;
}

/* ACCOUNT */

.account {
    position: absolute;
    left: 25px;
    bottom: 90px;
    color: white;
    display: flex;
    align-items: center;
    gap: 10px;
    z-index: 10;
}

.account-logo {
    width: 42px;
    height: 42px;
    background: white;
    color: #413bc0;
    border-radius: 50%;
    display: flex;
    justify-content: center;
    align-items: center;
    font-weight: bold;
}

.account b {
    font-size: 17px;
}

/* BUTTON */

.quote {
    position: absolute;
    bottom: 25px;
    left: 20px;
    right: 20px;
    height: 62px;
    border: none;
    border-radius: 18px;
    background: #6b6df0;
    color: white;
    font-size: 18px;
    font-weight: bold;
    cursor: pointer;
    z-index: 20;
    box-shadow: 0 4px 10px rgba(0,0,0,.2);
}

.quote span {
    position: absolute;
    right: 25px;
    font-size: 32px;
}

.quote:hover {
    background: #514fd0;
    transform: translateY(-2px);
}

/* RESPONSIVE */

@media (max-width: 450px) {

    .ad-container {
        width: 100%;
    }

    .heading h1 {
        font-size: 38px;
    }

    .heading p {
        font-size: 25px;
    }

    .trial {
        left: 25px;
    }

}

</style>
</head>

<body>

<div class="ad-container">

    <!-- LOGO -->
    <div class="logo">
        <div class="logo-symbol">dp</div>
        <span>drink prime</span>
    </div>

    <!-- HEADING -->
    <div class="heading">
        <h1>PURE WATER</h1>
        <p>with <span>Goodness</span> of Copper</p>
    </div>

    <!-- OFFER -->
    <div class="offer">

        <div class="offer-title">
            NOW GET <b>UNLIMITED WATER</b>
        </div>

        <div class="price">
            Starts at just <strong>₹349</strong>/month
        </div>

    </div>

    <!-- ZERO COST -->
    <div class="zero-cost">

        <div class="zero">₹0</div>

        <div class="cost-list">
            Maintenance Cost<br>
            Installation Cost<br>
            Machine cost
        </div>

    </div>

    <!-- TRIAL -->
    <div class="trial">
        <div class="number">7</div>
        <small>DAY FREE</small>
        <strong>TRIAL</strong>
    </div>

    <!-- WATER -->
    <div class="water"></div>

    <!-- PURIFIER -->
    <div class="purifier">

        <div class="display">
            <div></div>
            <div></div>
            <div></div>
        </div>

        <div class="tap"></div>

        <div class="copper c1">Cu</div>
        <div class="copper c2">Cu</div>
        <div class="copper c3">Cu</div>
        <div class="copper c4">Cu</div>
        <div class="copper c5">Cu</div>

    </div>

    <!-- PERSON -->
    <div class="person">

        <div class="hair"></div>
        <div class="head"></div>
        <div class="body"></div>
        <div class="shirt-line"></div>
        <div class="arm"></div>

        <div class="glass"></div>

    </div>

    <!-- ACCOUNT -->
    <div class="account">
        <div class="account-logo">dp</div>
        <b>drink_prime</b>
    </div>

    <!-- SOCIAL -->
    <div class="social">
        <div>♡<small>1316</small></div>
        <div>◯<small>28</small></div>
        <div>▷</div>
    </div>

    <!-- BUTTON -->
    <button class="quote" onclick="getQuote()">
        Get quote
        <span>›</span>
    </button>

</div>

<script>

function getQuote() {
    alert(
        "Thank you for your interest in Drink Prime!\\n\\n" +
        "Our team will contact you shortly."
    );
}

</script>

</body>
</html>
  `);
});

app.listen(PORT, () => {
    console.log("=================================");
    console.log(" Drink Prime Website Started");
    console.log("=================================");
    console.log("Open: http://localhost:" + PORT);
});