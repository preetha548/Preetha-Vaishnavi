const express = require("express");
const app = express();

app.get("/", (req, res) => {
  res.send(`
  <!DOCTYPE html>
  <html>
  <head>
      <title>Homemade Tomato Ketchup</title>
      <style>
          body{
              font-family: Arial, sans-serif;
              background:#f4f4f4;
              padding:40px;
          }

          .container{
              max-width:800px;
              margin:auto;
              background:white;
              padding:30px;
              border-radius:10px;
              box-shadow:0 0 10px rgba(0,0,0,0.2);
          }

          h1{
              color:#d62828;
              text-align:center;
          }

          h2{
              color:#333;
          }

          ul,ol{
              line-height:1.8;
          }

          img{
              width:100%;
              max-height:350px;
              object-fit:cover;
              border-radius:10px;
              margin-bottom:20px;
          }
      </style>
  </head>
  <body>

  <div class="container">

      <h1>🍅 Homemade Tomato Ketchup</h1>

      <img src="https://images.unsplash.com/photo-1601050690597-df0568f70950?w=1200"
           alt="Tomato Ketchup">

      <h2>Ingredients</h2>

      <ul>
          <li>1 kg Tomatoes</li>
          <li>1 Onion</li>
          <li>4 Garlic Cloves</li>
          <li>1/2 Cup Sugar</li>
          <li>1 tsp Salt</li>
          <li>1/2 Cup Vinegar</li>
          <li>1/2 tsp Black Pepper</li>
      </ul>

      <h2>Preparation Steps</h2>

      <ol>
          <li>Wash and chop tomatoes.</li>
          <li>Cook tomatoes, onion and garlic.</li>
          <li>Blend into a smooth puree.</li>
          <li>Strain the mixture.</li>
          <li>Add sugar, salt and spices.</li>
          <li>Cook until thick.</li>
          <li>Add vinegar and simmer.</li>
          <li>Cool and store in bottles.</li>
      </ol>

      <h2>Storage</h2>

      <p>
      Store in the refrigerator for 2–3 weeks.
      Use a clean spoon every time.
      </p>

  </div>

  </body>
  </html>
  `);
});

app.listen(3000, () => {
  console.log("Server running at http://localhost:3000");
});