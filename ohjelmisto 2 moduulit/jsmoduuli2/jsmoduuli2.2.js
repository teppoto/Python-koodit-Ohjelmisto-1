let osallistujat = parseInt(prompt("Anna osallistujien lukumäärä: "))
let olista = []

const target = document.querySelector('#target');
const ol = document.createElement("ol")

for (let i = 0; i < osallistujat; i++) {
  olista.push(prompt("Anna osallistuja nimi: "))
  olista.sort();
}

for (let i = 0; i < olista.length; i++) {
  const li = document.createElement('li');
  li.textContent = olista[i];
  ol.appendChild(li);
}

target.innerHTML = "";
target.appendChild(ol);




