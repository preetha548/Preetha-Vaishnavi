function predictLeak() {

    let gas = parseFloat(document.getElementById("gas").value);
    let temp = parseFloat(document.getElementById("temp").value);
    let pressure = parseFloat(document.getElementById("pressure").value);

    let result = document.getElementById("result");

    if(isNaN(gas)||isNaN(temp)||isNaN(pressure)){
        result.innerHTML="<h3>Please enter all sensor values.</h3>";
        return;
    }

    let probability=((gas/1000)*60)+((temp/100)*25)+((pressure/150)*15);

    if(probability>100)
        probability=100;

    probability=probability.toFixed(1);

    let risk="";
    let color="";
    let message="";
    let action="";
    let leakSize="";
    let location="";

    if(probability>=80){

        risk="🔴 CRITICAL";
        color="#d32f2f";
        message="Leakage Detected";
        leakSize="Large";
        location="Pipeline Section B";

        action=`
        ✔ Shut Down Pipeline Immediately<br>
        ✔ Activate Emergency Alarm<br>
        ✔ Inform Safety Team<br>
        ✔ Evacuate Nearby Workers<br>
        ✔ Start Fire Suppression System
        `;

    }
    else if(probability>=50){

        risk="🟠 WARNING";
        color="#ff9800";
        message="Possible Leakage";
        leakSize="Medium";
        location="Pipeline Section A";

        action=`
        ✔ Inspect Pipeline<br>
        ✔ Reduce Pressure<br>
        ✔ Continue Monitoring
        `;

    }
    else{

        risk="🟢 SAFE";
        color="#2e7d32";
        message="No Leakage";
        leakSize="None";
        location="No Leak";

        action=`
        ✔ Pipeline Operating Normally
        `;
    }

    let today=new Date();

    result.innerHTML=`

<div style="background:${color};color:white;padding:25px;border-radius:10px;margin-top:20px;">

<h2>Oil & Gas Leakage Report</h2>

<hr>

<p><b>Leak Probability :</b> ${probability}%</p>

<p><b>Risk Level :</b> ${risk}</p>

<p><b>Gas Level :</b> ${gas} ppm</p>

<p><b>Temperature :</b> ${temp} °C</p>

<p><b>Pressure :</b> ${pressure} kPa</p>

<p><b>Pipeline Status :</b> ${message}</p>

<p><b>Estimated Leak Size :</b> ${leakSize}</p>

<p><b>Estimated Location :</b> ${location}</p>

<p><b>Sensor Health :</b> Active</p>

<p><b>Time :</b> ${today.toLocaleString()}</p>

<h3>Recommended Actions</h3>

${action}

</div>

`;

}