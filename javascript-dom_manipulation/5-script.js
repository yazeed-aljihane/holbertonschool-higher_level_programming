const change = document
  .getElementById("update_header")
  .addEventListener("click", function () {
    const header = document.querySelector("header");
    header.innerHTML = "New Header!!!";
  });
