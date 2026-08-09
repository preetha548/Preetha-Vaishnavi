// ================================
// Carousel
// ================================

const slides = document.querySelector(".slides");
const cards = document.querySelectorAll(".marketing-card");

const nextBtn = document.querySelector(".next");
const prevBtn = document.querySelector(".prev");

let currentSlide = 0;

function updateCarousel() {

    const cardWidth = cards[0].getBoundingClientRect().width;

    const gap = 15;

    slides.style.transform =
        `translateX(-${currentSlide * (cardWidth + gap)}px)`;
}


nextBtn.addEventListener("click", () => {

    if (currentSlide < cards.length - 1) {
        currentSlide++;
    } else {
        currentSlide = 0;
    }

    updateCarousel();
});


prevBtn.addEventListener("click", () => {

    if (currentSlide > 0) {
        currentSlide--;
    } else {
        currentSlide = cards.length - 1;
    }

    updateCarousel();
});


window.addEventListener("resize", updateCarousel);


// ================================
// Like button
// ================================

const likeButton = document.querySelector(".like-btn");
const likeCount = document.getElementById("likeCount");

let liked = false;
let count = 6;

likeButton.addEventListener("click", () => {

    liked = !liked;

    if (liked) {
        count++;
        likeButton.classList.add("liked");
        likeButton.querySelector("label").textContent = "Liked";
    } else {
        count--;
        likeButton.classList.remove("liked");
        likeButton.querySelector("label").textContent = "Like";
    }

    likeCount.textContent = count;
});


// ================================
// Repost
// ================================

const repostButton = document.querySelector(".repost-btn");

repostButton.addEventListener("click", () => {

    const label = repostButton.querySelector("label");

    if (label.textContent === "Repost") {
        label.textContent = "Reposted";
        repostButton.classList.add("liked");
    } else {
        label.textContent = "Repost";
        repostButton.classList.remove("liked");
    }
});


// ================================
// Send
// ================================

const sendButton = document.querySelector(".send-btn");

sendButton.addEventListener("click", async () => {

    const shareData = {
        title: "Marketing In 2026",
        text: "Marketing in 2026 - AI answers."
    };

    try {

        if (navigator.share) {
            await navigator.share(shareData);
        } else {
            await navigator.clipboard.writeText(
                "Marketing in 2026 - AI answers."
            );

            alert("Post text copied!");
        }

    } catch (error) {
        console.log("Share cancelled");
    }

});


// ================================
// Navigation tabs
// ================================

const tabs = document.querySelectorAll(".tabs button");

tabs.forEach(tab => {

    tab.addEventListener("click", () => {

        tabs.forEach(item => {
            item.classList.remove("active");
        });

        tab.classList.add("active");

    });

});


// ================================
// More buttons
// ================================

document.querySelectorAll(".more").forEach(button => {

    button.addEventListener("click", () => {

        alert(
            "Post options\n\n" +
            "• Save post\n" +
            "• Copy link\n" +
            "• Hide post\n" +
            "• Report post"
        );

    });

});


// Initial position
updateCarousel();
