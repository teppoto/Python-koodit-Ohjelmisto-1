
lista = ["Johnny", "DeeDee", "Joey", "Marky"]

function concat(lista) {
  let tulos ="";
  for(let i = 0; i < lista.length; i++) {
    tulos += lista[i];
  }
  return tulos;
}

document.querySelector('#target').innerHTML = concat(lista);