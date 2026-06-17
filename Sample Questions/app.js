const express = require("express");
const app = express();

app.get("/", (req, res) => {
  res.send(`
<!DOCTYPE html>
<html>
<head>
    <title>Teacher Interview Questions</title>

    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">

    <style>
        body{
            background:#f4f4f4;
            font-family:Arial, sans-serif;
        }

        .container-box{
            max-width:1000px;
            margin:40px auto;
            background:white;
            padding:40px;
            border-radius:15px;
            box-shadow:0 0 15px rgba(0,0,0,0.1);
        }

        h1{
            text-align:center;
            color:#1d3f72;
            font-weight:bold;
            margin-bottom:40px;
        }

        ol li{
            margin-bottom:12px;
            font-size:17px;
            line-height:1.6;
        }
    </style>
</head>

<body>

<div class="container">
    <div class="container-box">

        <h1>SAMPLE INTERVIEW QUESTIONS FOR TEACHERS</h1>

        <ol>
            <li>The vision for our school is ____________. How do you see yourself contributing to that vision?</li>

            <li>What is your professional and personal commitment to diversity in the classroom?</li>

            <li>What student activities might you coach or advise as a member of the teaching staff?</li>

            <li>When did you decide to become a teacher, and why did you choose this field?</li>

            <li>Why do you want to teach at the elementary/middle/high school level?</li>

            <li>What personal strengths do you find especially helpful in your teaching?</li>

            <li>What is your favorite subject to teach? Why?</li>

            <li>What is your least favorite subject, and how do you overcome your indifference toward it?</li>

            <li>What do you like most about teaching as a career?</li>

            <li>What is your least favorite aspect of teaching?</li>

            <li>What is your philosophy of education? Of learning?</li>

            <li>What role do standards play in your classroom?</li>

            <li>Using examples, please describe your teaching style.</li>

            <li>Please describe how you organize your classroom.</li>

            <li>How do you structure your time to manage all teaching duties?</li>

            <li>What is the greatest success you have had in teaching?</li>

            <li>What do you think is the greatest challenge facing students today?</li>

            <li>What is the most difficult aspect of teaching today?</li>

            <li>What are the qualities of an excellent teacher?</li>

            <li>Describe the worst lesson you have taught. What did you learn from it?</li>

            <li>What is your approach to classroom management?</li>

            <li>What role have parents played in your classroom?</li>

            <li>How do you motivate students to become active learners?</li>

            <li>Tell us about a high-needs student you have taught and how you helped him or her.</li>

            <li>Describe your ideal lesson.</li>

            <li>Describe your planning process for a major project or unit.</li>

            <li>How have you integrated technology into your teaching instruction?</li>

            <li>What plans do you have for integrating technology in the classroom?</li>

            <li>What experience have you had with team-teaching?</li>

            <li>How do you address students' different learning styles?</li>

            <li>How do assignments allow students to express creativity and individuality?</li>

            <li>How do you modify teaching for struggling students?</li>

            <li>How do you provide support for students with exceptional ability?</li>
        </ol>

    </div>
</div>

</body>
</html>
  `);
});

app.listen(3000, () => {
    console.log("Server running on http://localhost:3000");
});