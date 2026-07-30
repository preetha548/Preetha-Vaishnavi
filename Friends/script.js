
// Clock

setInterval(()=>{

let time=new Date();

document.getElementById("clock")
.innerHTML=time.toLocaleTimeString();

},1000);




// Theme

function themeChange(){

document.body.classList.toggle("dark");

}



// Like System

function like(btn){

let count=
btn.querySelector("span");

count.innerHTML=
Number(count.innerHTML)+1;

}




// Comment System


function comment(btn){

let input=
btn.previousElementSibling;


let text=input.value;


if(text!=""){


let div=
btn.parentElement
.nextElementSibling;


div.innerHTML+=
"<p>💬 "+text+"</p>";


input.value="";


}

}




// Search


function searchFriend(){

let value=
document.getElementById("search")
.value.toLowerCase();


let cards=
document.getElementsByClassName(
"friend-card"
);



for(let card of cards){


let name=
card.querySelector("h2")
.innerHTML.toLowerCase();



if(name.includes(value))

card.style.display="block";


else

card.style.display="none";


}


}



// Popup


function openForm(){

document.getElementById("popup")
.style.display="block";

}



function closeForm(){

document.getElementById("popup")
.style.display="none";

}



// Add Friend


function addFriend(){


let name=
document.getElementById("name").value;


let job=
document.getElementById("job").value;


let image=
document.getElementById("image").value;



let card=document.createElement("div");


card.className="friend-card";


card.innerHTML=`

<img src="${image}">

<h2>${name}</h2>

<p>${job}</p>

<p>
⭐ Friendship Level : 80%
</p>


<button onclick="like(this)">
❤️ <span>0</span>
</button>


<div>

<input class="commentInput"
placeholder="Write comment">


<button onclick="comment(this)">
Comment
</button>

</div>


<div class="comments"></div>

`;



document.getElementById("friendList")
.appendChild(card);



closeForm();


}


// Save theme preference

localStorage.setItem(
"website",
"Friends Hub"
);
