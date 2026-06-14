async function register() {

    const name = document.getElementById("name").value;
    const age = document.getElementById("age").value;
    const city = document.getElementById("city").value;

    const response = await fetch("/register", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            name,
            age,
            city
        })
    });

    const data = await response.json();

    alert(data.message);

    loadParticipants();
}

async function loadParticipants() {

    const response = await fetch("/participants");
    const participants = await response.json();

    const list = document.getElementById("list");

    list.innerHTML = "";

    participants.forEach(p => {
        const li = document.createElement("li");
        li.textContent =
            `${p.name} | ${p.age} Years | ${p.city}`;
        list.appendChild(li);
    });
}

loadParticipants();