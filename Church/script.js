

// MOBILE NAVIGATION

const menuBtn = document.getElementById("menuBtn");
const navbar = document.getElementById("navbar");

menuBtn.addEventListener("click", function() {

    navbar.classList.toggle("active");

    const isOpen = navbar.classList.contains("active");

    menuBtn.textContent = isOpen ? "✕" : "☰";

    menuBtn.setAttribute("aria-expanded", String(isOpen));

});

// CLOSE MENU AFTER CLICKING

document.querySelectorAll("#navbar a").forEach(function(link) {

    link.addEventListener("click", function() {

        navbar.classList.remove("active");

        menuBtn.textContent = "☰";

        menuBtn.setAttribute("aria-expanded", "false");

    });

});

// CURRENT YEAR

document.getElementById("year").textContent =
    new Date().getFullYear();

// CONTACT FORM

document.getElementById("contactForm")
.addEventListener("submit", function(event) {

    event.preventDefault();

    const name = document.getElementById("name").value;

    document.getElementById("response").textContent =
        "Thank you " + name +
        "! Your message has been received in this demo.";

    this.reset();

});

// BACK TO TOP

const backToTop = document.getElementById("backToTop");

window.addEventListener("scroll", function() {

    if (window.scrollY > 300) {

        backToTop.classList.add("show");

    } else {

        backToTop.classList.remove("show");

    }

});

backToTop.addEventListener("click", function() {

    window.scrollTo({
        top: 0,
        behavior: "smooth"
    });

});
