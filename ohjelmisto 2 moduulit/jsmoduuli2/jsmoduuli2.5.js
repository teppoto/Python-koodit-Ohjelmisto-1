let numerolista = [];

while (true) {
  let numero = prompt("Anna numero: ");

  if (numerolista.includes(numero)) {
    document.querySelector('#target').innerHTML = "Numero on jo annettu, ohjelma pysäytettiin";
    console.log("Annetut numerot järjestyksessä: ", numerolista.sort((a, b) => a - b));
    break;
  } else {
    numerolista.push(numero);
  }
}
