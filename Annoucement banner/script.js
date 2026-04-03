let index = 0;
let slides = document.getElementsByClassName("banner");

function showSlide(i){

for(let s of slides){
s.style.display = "none";
}

slides[i].style.display = "block";
}

function changeSlide(step){
index += step;

if(index >= slides.length){
index = 0;
}

if(index < 0){
index = slides.length - 1;
}

showSlide(index);
}

setInterval(function(){
changeSlide(1);
},3000);