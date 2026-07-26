const rows = 15;
const cols = 15;

const letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

const grid = document.getElementById("grid");

const leftWords = [
"Firework",
"Happy",
"Royals",
"Dynamite",
"Roar",
"Lasting",
"Liv It Up",
"Despacito",
"Closer",
"Perfect",
"Sunflower",
"Senorita",
"Havana",
"Stay",
"Shallow",
"Sorry",
"Memories"
];

const rightWords=[
"Shake It Off",
"Uptown Funk",
"Shape of You",
"Bad Romance",
"Call Me Maybe",
"Blinding Lights",
"Counting Stars",
"Old Town Road",
"Someone Like You",
"Watermelon Sugar",
"Rolling in the Deep",
"We Don't Talk Anymore"
];

function fillLists(){

leftWords.forEach(word=>{

const li=document.createElement("li");
li.textContent=word;
document.getElementById("leftWords").appendChild(li);

});

rightWords.forEach(word=>{

const li=document.createElement("li");
li.textContent=word;
document.getElementById("songWords").appendChild(li);

});

}

fillLists();

for(let r=0;r<rows;r++){

for(let c=0;c<cols;c++){

const cell=document.createElement("div");
cell.className="cell";

cell.textContent=letters[Math.floor(Math.random()*letters.length)];

grid.appendChild(cell);

}

}

let drawing=false;

grid.addEventListener("mousedown",()=>drawing=true);

document.addEventListener("mouseup",()=>drawing=false);

grid.addEventListener("mouseover",e=>{

if(!drawing)return;

if(e.target.classList.contains("cell")){

e.target.classList.toggle("selected");

}

});

grid.addEventListener("click",e=>{

if(e.target.classList.contains("cell")){

e.target.classList.toggle("selected");

}

});