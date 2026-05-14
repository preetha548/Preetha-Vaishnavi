const bulb = document.getElementById("bulb");
const toggleBtn = document.getElementById("toggleBtn");

let isOn = false;

toggleBtn.addEventListener("click", () => {
  isOn = !isOn;

  if (isOn) {
    bulb.classList.remove("off");
    bulb.classList.add("on");
    toggleBtn.textContent = "Turn OFF";
    document.body.style.background = "#222";
  } else {
    bulb.classList.remove("on");
    bulb.classList.add("off");
    toggleBtn.textContent = "Turn ON";
    document.body.style.background = "#111";
  }
});
