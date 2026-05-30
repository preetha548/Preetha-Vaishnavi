let seconds = 0;
let timerStarted = false;

setTimeout(() => {
    document.getElementById("status").innerText = "Connected";
    timerStarted = true;
}, 3000);

setInterval(() => {
    if(timerStarted){
        seconds++;

        let min = Math.floor(seconds / 60);
        let sec = seconds % 60;

        document.getElementById("timer").innerText =
            String(min).padStart(2, "0") + ":" +
            String(sec).padStart(2, "0");
    }
}, 1000);

function endCall(){
    document.getElementById("status").innerText = "Call Ended";
    timerStarted = false;
}