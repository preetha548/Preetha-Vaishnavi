const fields = [
    "occasion",
    "datetime",
    "theme",
    "food",
    "decor",
    "cake",
    "invite",
    "music",
    "loot",
    "games",
    "reminders"
];

window.onload = function () {
    loadData();
};

function saveData() {

    fields.forEach(id => {
        localStorage.setItem(id, document.getElementById(id).value);
    });

    alert("Party plan saved!");
}

function loadData() {

    fields.forEach(id => {
        const value = localStorage.getItem(id);
        if(value){
            document.getElementById(id).value = value;
        }
    });

}

function clearData(){

    if(confirm("Clear the planner?")){

        fields.forEach(id=>{
            localStorage.removeItem(id);
            document.getElementById(id).value="";
        });

    }

}
