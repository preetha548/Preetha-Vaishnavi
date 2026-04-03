document.getElementById("newsletterForm").addEventListener("submit", function(e){

    e.preventDefault();

    let email = document.getElementById("email").value;
    let message = document.getElementById("message");

    let emailPattern = /^[^ ]+@[^ ]+\.[a-z]{2,3}$/;

    if(email.match(emailPattern)){
        message.style.color = "green";
        message.innerHTML = "✅ Successfully subscribed!";
    }
    else{
        message.style.color = "red";
        message.innerHTML = "❌ Please enter a valid email address";
    }

});