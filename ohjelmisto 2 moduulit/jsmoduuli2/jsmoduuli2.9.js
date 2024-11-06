
let lista = [2, 7, 4]

function even(lista) {
  let evens = [];

  for (let i = 0; i < lista.length; i++) {
    if (lista[i] % 2 === 0) {
      evens.push(lista[i]);
    }
  }
  return evens;
}

console.log("Alkuperäinen lista: ", lista);
console.log("Uusi lista: ", even(lista));
