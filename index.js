//import "./styles.css";

// document.getElementById("app").innerHTML = `
// <h1>Hello Vanilla!</h1>
// <div>
//   We use the same configuration as Parcel to bundle this sandbox, you can find more
//   info about Parcel
//   <a href="https://parceljs.org" target="_blank" rel="noopener noreferrer">here</a>.
// </div>
// `;

console.log("Happy Hacking");

//const URL = "https://rickandmortyapi.com/api";
const URL = "https://api.thecatapi.com/v1/images/search";

fetch(URL)
  .then((res) => res.json())
  .then((data) => {
    const img = document.querySelector("img");
    //img.src = data.character.results[0].name;
    img.src = data[0].url;
  });
