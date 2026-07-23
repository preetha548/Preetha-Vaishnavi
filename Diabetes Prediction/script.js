let reportData={};


function predict(){


let name=document.getElementById("name").value;

let age=Number(document.getElementById("age").value);

let glucose=Number(document.getElementById("glucose").value);

let bp=Number(document.getElementById("bp").value);

let bmi=Number(document.getElementById("bmi").value);

let insulin=Number(document.getElementById("insulin").value);

let preg=Number(document.getElementById("preg").value);

let dpf=Number(document.getElementById("dpf").value);



if(!name || !age || !glucose || !bmi){

alert("Please fill required fields");

return;

}



let score=0;


if(glucose>140)
score+=35;

if(bmi>30)
score+=25;

if(age>45)
score+=15;

if(bp>90)
score+=10;

if(insulin>150)
score+=5;

if(preg>5)
score+=5;

if(dpf>0.6)
score+=5;



let status;


if(score<35)
status="Low Risk";

else if(score<65)
status="Moderate Risk";

else
status="High Risk";



document.getElementById("result").innerHTML=

"Prediction: "+status+
"<br>Risk Score: "+score+"%";



reportData={

name:name,
age:age,
glucose:glucose,
bp:bp,
bmi:bmi,
insulin:insulin,
preg:preg,
dpf:dpf,
status:status,
score:score,
date:new Date().toLocaleString()

};


}



function generatePDF(){


if(!reportData.name){

alert("Please predict first");

return;

}



const {jsPDF}=window.jspdf;


let pdf=new jsPDF();



pdf.setFontSize(18);

pdf.text(
"Diabetes Prediction Report",
20,
20
);



pdf.setFontSize(12);


pdf.text(
"Patient Name: "+reportData.name,
20,
40
);


pdf.text(
"Age: "+reportData.age,
20,
50
);


pdf.text(
"Glucose: "+reportData.glucose,
20,
60
);


pdf.text(
"BMI: "+reportData.bmi,
20,
70
);


pdf.text(
"Blood Pressure: "+reportData.bp,
20,
80
);


pdf.text(
"Insulin: "+reportData.insulin,
20,
90
);


pdf.text(
"Risk Status: "+reportData.status,
20,
110
);


pdf.text(
"Risk Score: "+reportData.score+"%",
20,
120
);


pdf.text(
"Generated Date: "+reportData.date,
20,
140
);



pdf.text(
"Note: This is a risk estimation system and not a medical diagnosis.",
20,
160
);



pdf.save(
"Diabetes_Report.pdf"
);


}
