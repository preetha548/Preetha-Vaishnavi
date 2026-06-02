document
.getElementById("bookingForm")
.addEventListener("submit", function(e){

e.preventDefault();

document.getElementById("message")
.innerHTML =
`<div class="alert alert-success">
Booking Successful!
</div>`;

});