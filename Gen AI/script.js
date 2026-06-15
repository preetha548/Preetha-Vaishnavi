const responses = {
    "hello":"Hello! Welcome to the Generative AI Demo.",
    "hi":"Hi! How can I help you today?",
    "good morning":"Good morning! Have a great day.",
    "good afternoon":"Good afternoon! How may I assist you?",
    "good evening":"Good evening! What would you like to know?",

    "what is ai":"Artificial Intelligence (AI) enables machines to simulate human intelligence.",
    "what is generative ai":"Generative AI creates text, images, videos, music, and code based on user prompts.",
    "what is machine learning":"Machine Learning is a branch of AI that allows systems to learn from data.",
    "what is deep learning":"Deep Learning uses neural networks to process complex data patterns.",
    "what is data science":"Data Science is the study of extracting insights from data.",

    "what is html":"HTML stands for HyperText Markup Language.",
    "what is css":"CSS is used to style web pages.",
    "what is javascript":"JavaScript is used to create interactive web pages.",
    "what is react":"React is a JavaScript library for building user interfaces.",
    "what is node js":"Node.js allows JavaScript to run on the server side.",
    "what is express js":"Express.js is a web framework for Node.js.",
    "what is mongodb":"MongoDB is a NoSQL database.",
    "what is mern":"MERN stands for MongoDB, Express.js, React, and Node.js.",

    "what is java":"Java is a popular object-oriented programming language.",
    "what is python":"Python is a versatile programming language widely used in AI and Data Science.",
    "what is c":"C is a powerful procedural programming language.",
    "what is c++":"C++ is an extension of the C programming language.",
    "what is kotlin":"Kotlin is a modern language used for Android development.",

    "what is cloud computing":"Cloud Computing provides computing services over the internet.",
    "what is aws":"AWS is Amazon's cloud computing platform.",
    "what is cybersecurity":"Cybersecurity protects systems and networks from digital attacks.",
    "what is blockchain":"Blockchain is a decentralized digital ledger technology.",
    "what is iot":"IoT stands for Internet of Things.",

    "who are you":"I am a demo AI assistant.",
    "how are you":"I am doing great. Thanks for asking!",
    "what can you do":"I can answer basic questions and provide information.",
    "tell me a joke":"Why do programmers prefer dark mode? Because light attracts bugs!",
    "tell me a fact":"The first computer bug was an actual moth found in a computer.",

    "what is digital marketing":"Digital marketing promotes products and services online.",
    "what is seo":"SEO stands for Search Engine Optimization.",
    "what is social media marketing":"It is the use of social media platforms for marketing purposes.",
    "what is content marketing":"Content marketing focuses on creating valuable content for audiences.",

    "what is finance":"Finance deals with managing money and investments.",
    "what is banking":"Banking involves accepting deposits and providing financial services.",
    "what is fintech":"FinTech combines finance and technology to improve financial services.",

    "what is operation management":"Operations Management focuses on planning and controlling business operations.",
    "what is project management":"Project Management involves planning, executing, and completing projects successfully.",

    "what is a database":"A database is an organized collection of data.",
    "what is sql":"SQL is used to manage relational databases.",
    "what is dbms":"DBMS stands for Database Management System.",

    "what is an operating system":"An operating system manages computer hardware and software resources.",
    "what is windows":"Windows is an operating system developed by Microsoft.",
    "what is linux":"Linux is an open-source operating system.",

    "what is a computer":"A computer is an electronic device that processes data.",
    "what is software":"Software is a set of instructions that tells a computer what to do.",
    "what is hardware":"Hardware refers to the physical components of a computer.",

    "thank you":"You're welcome!",
    "thanks":"Happy to help!",
    "bye":"Goodbye! Have a wonderful day.",
    "see you":"See you again soon!"
};

function sendMessage(){

    let input = document.getElementById("userInput");
    let chatbox = document.getElementById("chatbox");

    let text = input.value.trim();

    if(text === ""){
        return;
    }

    let userDiv = document.createElement("div");
    userDiv.className = "user-message";
    userDiv.innerText = text;
    chatbox.appendChild(userDiv);

    input.value = "";

    let typing = document.createElement("div");
    typing.className = "bot-message";
    typing.innerText = "Typing...";
    chatbox.appendChild(typing);

    setTimeout(() => {

        typing.remove();

        let botDiv = document.createElement("div");
        botDiv.className = "bot-message";

        let reply =
            responses[text.toLowerCase()] ||
            "Sorry, I am a demo AI assistant. I can answer basic questions.";

        botDiv.innerText = reply;

        chatbox.appendChild(botDiv);

        chatbox.scrollTop = chatbox.scrollHeight;

    }, 1000);
}