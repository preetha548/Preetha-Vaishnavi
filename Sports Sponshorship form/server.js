const express = require("express");
const bodyParser = require("body-parser");
const path = require("path");

const app = express();

app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static("public"));

app.get("/", (req, res) => {
    res.sendFile(path.join(__dirname, "public", "index.html"));
});

app.post("/submit", (req, res) => {
    console.log(req.body);
    res.send("Application Submitted Successfully!");
});

app.listen(3000, () => {
    console.log("Server running at http://localhost:3000");
});