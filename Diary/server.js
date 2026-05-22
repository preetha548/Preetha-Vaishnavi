// server.js
const http = require("http");

const html = `
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>Moment & Diary</title>

<style>
    *{
        margin:0;
        padding:0;
        box-sizing:border-box;
        font-family: Arial, sans-serif;
    }

    body{
        background:#3f4654;
        display:flex;
        justify-content:center;
        align-items:center;
        min-height:100vh;
        flex-direction:column;
    }

    h1{
        color:white;
        font-size:70px;
        margin-bottom:40px;
        font-weight:300;
    }

    .phone{
        width:420px;
        background:#f5f5f5;
        border:12px solid #f0e4d5;
        border-radius:45px;
        padding:20px;
        position:relative;
        box-shadow:0 10px 30px rgba(0,0,0,0.4);
    }

    .top{
        height:40px;
        position:relative;
        margin-bottom:10px;
    }

    .camera{
        width:12px;
        height:12px;
        background:#333;
        border-radius:50%;
        position:absolute;
        left:35%;
        top:12px;
    }

    .speaker{
        width:80px;
        height:8px;
        background:#444;
        border-radius:10px;
        position:absolute;
        left:50%;
        transform:translateX(-50%);
        top:14px;
    }

    .screen{
        border:4px solid #333;
        background:white;
        overflow:hidden;
    }

    .header{
        background:#12c7c9;
        color:white;
        padding:15px;
        text-align:center;
    }

    .status{
        display:flex;
        justify-content:space-between;
        font-size:14px;
        margin-bottom:25px;
    }

    .menu-top{
        display:flex;
        justify-content:space-around;
        align-items:center;
        padding:20px 0;
    }

    .menu-box{
        text-align:center;
        width:45%;
    }

    .icon{
        font-size:50px;
        margin-bottom:10px;
    }

    .menu-box h2{
        font-weight:300;
    }

    .divider{
        width:1px;
        background:rgba(255,255,255,0.5);
        height:90px;
    }

    .stats{
        display:flex;
        justify-content:space-around;
        padding:15px 0 5px;
        font-size:14px;
    }

    .stats div{
        text-align:center;
    }

    .stats span{
        display:block;
        font-size:13px;
        margin-top:5px;
    }

    .list{
        background:white;
    }

    .item{
        display:flex;
        justify-content:space-between;
        align-items:center;
        padding:22px;
        border-bottom:1px solid #b9ecec;
    }

    .left{
        display:flex;
        align-items:center;
        gap:18px;
    }

    .left-icon{
        font-size:28px;
        color:#12c7c9;
    }

    .text h3{
        color:#0c8f92;
        margin-bottom:4px;
        font-weight:400;
    }

    .text p{
        color:#5da8aa;
        font-size:15px;
    }

    .arrow{
        color:#12c7c9;
        font-size:30px;
    }
</style>
</head>

<body>

<h1>Moment & Diary</h1>

<div class="phone">

    <div class="top">
        <div class="camera"></div>
        <div class="speaker"></div>
    </div>

    <div class="screen">

        <div class="header">

            <div class="status">
                <span>Carrier 📶</span>
                <span>10:25 AM</span>
                <span>🔋</span>
            </div>

            <div class="menu-top">

                <div class="menu-box">
                    <div class="icon">💧</div>
                    <h2>Moment</h2>
                </div>

                <div class="divider"></div>

                <div class="menu-box">
                    <div class="icon">📝</div>
                    <h2>Diary</h2>
                </div>

            </div>

            <div class="stats">
                <div>11<span>MOMENT</span></div>
                <div>8<span>DIARY</span></div>
                <div>0<span>THIS MONTH</span></div>
                <div>0<span>TODAY</span></div>
            </div>

        </div>

        <div class="list">

            <div class="item">
                <div class="left">
                    <div class="left-icon">📋</div>
                    <div class="text">
                        <h3>Timeline</h3>
                        <p>Journal your thoughts</p>
                    </div>
                </div>
                <div class="arrow">›</div>
            </div>

            <div class="item">
                <div class="left">
                    <div class="left-icon">📷</div>
                    <div class="text">
                        <h3>Photos</h3>
                        <p>Slideshow in landscape mode</p>
                    </div>
                </div>
                <div class="arrow">›</div>
            </div>

            <div class="item">
                <div class="left">
                    <div class="left-icon">📅</div>
                    <div class="text">
                        <h3>Calendar</h3>
                        <p>Search and organize by dates</p>
                    </div>
                </div>
                <div class="arrow">›</div>
            </div>

            <div class="item">
                <div class="left">
                    <div class="left-icon">✏️</div>
                    <div class="text">
                        <h3>Diaries</h3>
                        <p>All your moods and diaries</p>
                    </div>
                </div>
                <div class="arrow">›</div>
            </div>

            <div class="item">
                <div class="left">
                    <div class="left-icon">🔍</div>
                    <div class="text">
                        <h3>Search And Tags</h3>
                        <p>Organize your entries by keywords</p>
                    </div>
                </div>
                <div class="arrow">›</div>
            </div>

            <div class="item">
                <div class="left">
                    <div class="left-icon">⭐</div>
                    <div class="text">
                        <h3>Anniversary</h3>
                        <p>Record important days</p>
                    </div>
                </div>
                <div class="arrow">›</div>
            </div>

            <div class="item">
                <div class="left">
                    <div class="left-icon">⚙️</div>
                    <div class="text">
                        <h3>Settings</h3>
                    </div>
                </div>
                <div class="arrow">›</div>
            </div>

        </div>

    </div>

</div>

</body>
</html>
`;

const server = http.createServer((req, res) => {
    res.writeHead(200, { "Content-Type": "text/html" });
    res.end(html);
});

server.listen(3000, () => {
    console.log("Server running at http://localhost:3000");
});