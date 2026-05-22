// server.js
const http = require("http");

const server = http.createServer((req, res) => {
  res.writeHead(200, { "Content-Type": "text/html" });

  res.end(`
    <!DOCTYPE html>
    <html>
    <head>
      <title>Letter Box</title>
      <style>
        body {
          display: flex;
          justify-content: center;
          align-items: center;
          height: 100vh;
          background: #f2f2f2;
          margin: 0;
          font-family: Arial, sans-serif;
        }

        .letter-box {
          width: 300px;
          height: 200px;
          background: #ff4d4d;
          border-radius: 10px;
          position: relative;
          box-shadow: 0 5px 15px rgba(0,0,0,0.3);
        }

        .slot {
          width: 150px;
          height: 12px;
          background: #222;
          position: absolute;
          top: 30px;
          left: 75px;
          border-radius: 5px;
        }

        .letter {
          width: 180px;
          height: 100px;
          background: white;
          position: absolute;
          bottom: 20px;
          left: 60px;
          border-radius: 5px;
          transition: transform 0.5s;
        }

        .letter::before {
          content: "✉";
          font-size: 50px;
          position: absolute;
          top: 20px;
          left: 65px;
          color: #ff4d4d;
        }

        .letter-box:hover .letter {
          transform: translateY(-50px);
        }

        h1 {
          position: absolute;
          top: 20px;
          color: #333;
        }
      </style>
    </head>
    <body>

      <h1>Letter Box Animation</h1>

      <div class="letter-box">
        <div class="slot"></div>
        <div class="letter"></div>
      </div>

    </body>
    </html>
  `);
});

server.listen(3000, () => {
  console.log("Server running at http://localhost:3000");
});