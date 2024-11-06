let numerolista = [];

while (true) {
  let numero = prompt("Anna numero: ");

  if (numerolista.includes(numero)) {
    document.querySelector('#target').innerHTML = "Numero on jo annettu, katso konsoli";
    console.log(numerolista);
  }
  else {
    numerolista.push(numero);
    numerolista.sort((a, b) => a - b);
  }
}