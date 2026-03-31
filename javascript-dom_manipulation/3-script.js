let header = document.querySelector("header");
let toggleHeader = document
  .getElementById("toggle_header")
  .addEventListener("click", function () {
    if (header.classList.contains("red")) {
      header.classList.remove("red");
      header.classList.add("green");
    } else {
      header.classList.add("red");
      header.classList.remove("green");
    }
  });
