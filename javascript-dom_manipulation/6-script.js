const chracter = fetch("https://swapi-api.hbtn.io/api/people/5/?format=json")
  .then((response) => response.json())
  .then((data) => {
    const name = data.name;
    const ch = document.getElementById("character");
    ch.innerHTML = name;
  });
