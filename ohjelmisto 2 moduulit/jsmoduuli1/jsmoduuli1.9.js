let kokonaisluku = parseInt(prompt("Anna kokonaisluku: "));
let alkuluku = true;

if (kokonaisluku <= 1) {
  alkuluku = false;
} else {
  for (let luku = 2; luku < kokonaisluku; luku++) {
    if (kokonaisluku % luku === 0) {
      alkuluku = false;
      break;
    }
  }
}

if (alkuluku) {
  document.querySelector('#target').innerHTML = "On alkuluku"
} else {
  document.querySelector('#target').innerHTML = "Ei ole alkuluku"
}