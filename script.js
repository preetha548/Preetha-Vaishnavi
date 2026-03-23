const stairs = document.getElementById("stairs");
const person = document.getElementById("person");

// Create stairs dynamically
let stepCount = 10;
for (let i = 0; i < stepCount; i++) {
    let step = document.createElement("div");
    step.classList.add("step");
    step.style.marginLeft = i * 30 + "px";
    stairs.appendChild(step);
}

// Animation
function startClimb() {
    let step = 0;

    let interval = setInterval(() => {
        if (step >= stepCount) {
            clearInterval(interval);
            return;
        }

        person.style.left = step * 30 + "px";
        person.style.bottom = step * 25 + "px";

        step++;
    }, 500);
}