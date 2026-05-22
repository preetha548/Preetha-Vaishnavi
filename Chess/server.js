// server.js
// Simple Chess Board in Node.js using Express

const express = require("express");
const app = express();

app.get("/", (req, res) => {
  res.send(`
  <!DOCTYPE html>
  <html>
  <head>
    <title>Chess Board</title>
    <style>
      body{
        display:flex;
        justify-content:center;
        align-items:center;
        height:100vh;
        background:#222;
        margin:0;
        font-family:Arial;
      }

      .board{
        display:grid;
        grid-template-columns:repeat(8,80px);
        grid-template-rows:repeat(8,80px);
        border:5px solid white;
      }

      .square{
        width:80px;
        height:80px;
        display:flex;
        justify-content:center;
        align-items:center;
        font-size:40px;
      }

      .white{
        background:#f0d9b5;
      }

      .black{
        background:#b58863;
      }
    </style>
  </head>
  <body>

    <div class="board" id="board"></div>

    <script>
      const board = document.getElementById("board");

      const pieces = [
        ["♜","♞","♝","♛","♚","♝","♞","♜"],
        ["♟","♟","♟","♟","♟","♟","♟","♟"],
        ["","","","","","","",""],
        ["","","","","","","",""],
        ["","","","","","","",""],
        ["","","","","","","",""],
        ["♙","♙","♙","♙","♙","♙","♙","♙"],
        ["♖","♘","♗","♕","♔","♗","♘","♖"]
      ];

      for(let row=0; row<8; row++){
        for(let col=0; col<8; col++){

          const square = document.createElement("div");

          square.classList.add("square");

          if((row + col) % 2 === 0){
            square.classList.add("white");
          } else {
            square.classList.add("black");
          }

          square.innerHTML = pieces[row][col];

          board.appendChild(square);
        }
      }
    </script>

  </body>
  </html>
  `);
});

app.listen(3000, () => {
  console.log("Chess app running on http://localhost:3000");
});