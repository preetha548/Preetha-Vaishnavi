function generateCertificate(){

let p1 = document.getElementById("person1").value;
let p2 = document.getElementById("person2").value;
let place = document.getElementById("place").value;
let date = document.getElementById("date").value;
let officer = document.getElementById("officer").value;

let output = `
<b>${p1}</b> and <b>${p2}</b> were united in marriage<br>
at <b>${place}</b> on <b>${date}</b><br>
by <b>${officer}</b>.
`;

document.getElementById("result").innerHTML = output;

}