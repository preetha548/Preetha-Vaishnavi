
// ===================================
// SERVINGS ADJUSTMENT
// ===================================

const servings = document.getElementById("servings");

const original = {
    chickpeas: 2,
    tahini: 3,
    lemon: 0.5,
    garlic: 1,
    oil: 2
};

function updateServings() {

    const multiplier = Number(servings.value) / 10;

    document.querySelector('[data-ingredient="chickpeas"]')
        .textContent = `${original.chickpeas * multiplier} cups`;

    document.querySelector('[data-ingredient="tahini"]')
        .textContent = `${original.tahini * multiplier} tbsp`;

    document.querySelector('[data-ingredient="lemon"]')
        .textContent = `${original.lemon * multiplier} tbsp`;

    document.querySelector('[data-ingredient="garlic"]')
        .textContent =
        `${original.garlic * multiplier} clove${multiplier === 1 ? "" : "s"}`;

    document.querySelector('[data-ingredient="oil"]')
        .textContent = `${original.oil * multiplier} tbsp`;
}

servings.addEventListener("change", updateServings);


// ===================================
// INGREDIENT PROGRESS
// ===================================

const ingredients = document.querySelectorAll(
    '#ingredientList input[type="checkbox"]'
);

const ingredientBar = document.getElementById("ingredientBar");

const ingredientProgress =
    document.getElementById("ingredientProgress");

const ingredientPercent =
    document.getElementById("ingredientPercent");

function updateIngredients() {

    const completed = [...ingredients]
        .filter(item => item.checked).length;

    const percent = Math.round(
        completed / ingredients.length * 100
    );

    ingredientProgress.textContent =
        `${completed} of ${ingredients.length} ingredients ready`;

    ingredientPercent.textContent = `${percent}%`;

    ingredientBar.style.width = `${percent}%`;
}

ingredients.forEach(item => {
    item.addEventListener("change", updateIngredients);
});


// ===================================
// COOKING STEP PROGRESS
// ===================================

const steps = document.querySelectorAll(".step-check");

const stepCount = document.getElementById("stepCount");

function updateSteps() {

    const completed = [...steps]
        .filter(item => item.checked).length;

    stepCount.textContent =
        `${completed} / ${steps.length} completed`;

}

steps.forEach(step => {
    step.addEventListener("change", updateSteps);
});
