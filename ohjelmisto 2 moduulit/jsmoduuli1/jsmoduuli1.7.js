let noppa_maara = parseInt(prompt("Anna noppien määrä: "));

let noppaluvut = [];

for (let i = 0; i < noppa_maara; i++) {
    let noppa = Math.floor(Math.random() * 6) + 1;
    noppaluvut.push(noppa);
}

let sum = noppaluvut.reduce((accumulator, currentValue) => accumulator + currentValue, 0);

document.querySelector('#target').innerHTML = sum