const ullist = document.getElementsByClassName("my_list");
const additem = document
  .getElementById("add_item")
  .addEventListener("click", function () {
    const newli = document.createElement("li");
    newli.textContent = "Item";
    ullist[0].appendChild(newli);
  });
