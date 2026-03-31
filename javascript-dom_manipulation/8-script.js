const hello = fetch("https://hellosalut.stefanbohacek.com/?lang=fr")
  .then((response) => response.json())
  .then((data) => {
    const hello = data.hello;
    const h = document.getElementById("hello");
    h.innerHTML = hello;
  });
