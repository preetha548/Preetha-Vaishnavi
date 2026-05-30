const cards = document.querySelectorAll(".card");

cards.forEach(card => {
    card.addEventListener("click", () => {
        card.style.transform = "scale(1.05)";
        
        setTimeout(() => {
            card.style.transform = "";
        }, 300);

        alert("📸 Beautiful Candid Moment!");
    });
});