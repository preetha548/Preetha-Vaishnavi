const express = require("express");
const fs = require("fs");

const app = express();
const PORT = 3000;

app.use(express.json());
app.use(express.static("public"));

const filePath = "./data/participants.json";

app.post("/register", (req, res) => {
    const participant = req.body;

    let participants = [];

    if (fs.existsSync(filePath)) {
        participants = JSON.parse(fs.readFileSync(filePath));
    }

    participants.push(participant);

    fs.writeFileSync(filePath, JSON.stringify(participants, null, 2));

    res.json({
        message: "Registration Successful"
    });
});

app.get("/participants", (req, res) => {
    if (!fs.existsSync(filePath)) {
        return res.json([]);
    }

    const participants = JSON.parse(
        fs.readFileSync(filePath)
    );

    res.json(participants);
});

app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
});