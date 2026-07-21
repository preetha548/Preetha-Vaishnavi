function detectMilk(){

    let ph = Number(document.getElementById("ph").value);
    let fat = Number(document.getElementById("fat").value);
    let water = Number(document.getElementById("water").value);
    let urea = Number(document.getElementById("urea").value);
    let starch = Number(document.getElementById("starch").value);


    // Simple AI rule-based prediction model

    let score = 100;


    if(ph < 6.5 || ph > 6.9)
        score -= 20;

    if(fat < 3)
        score -= 20;

    if(water > 15)
        score -= 25;

    if(urea > 0)
        score -= 25;

    if(starch == 1)
        score -= 20;


    let result="";


    if(score >= 70){

        result = `
        ✅ Pure Milk<br>
        AI Confidence: ${score}%
        `;

        document.getElementById("result").style.color="green";

    }
    else{

        result = `
        ❌ Adulterated Milk<br>
        AI Confidence: ${100-score}%
        `;

        document.getElementById("result").style.color="red";
    }


    document.getElementById("result").innerHTML=result;

}
