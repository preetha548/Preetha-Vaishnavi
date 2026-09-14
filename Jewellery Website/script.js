/* Navigation behavior for the credited jewellery frontend adaptation. */
$(function () {
  const $root = $("html, body");
  const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)");

  // Restrict scrolling to real local anchors. External links keep normal behavior.
  $("a[href^='#']").on("click", function (event) {
    const id = this.getAttribute("href").slice(1);
    const target = document.getElementById(id);
    if (!target) return;
    event.preventDefault();
    $root.stop().animate({ scrollTop: $(target).offset().top }, reducedMotion.matches ? 0 : 800);
    if ($(this).closest("nav").length) {
      $("nav li a").removeClass("active");
      $(this).addClass("active");
    }
  });

  function updateStickyNavigation() {
    $("nav").toggleClass("nav-sticky", $(window).scrollTop() > 185);
  }
  $(window).on("scroll", updateStickyNavigation);
  updateStickyNavigation();
});
