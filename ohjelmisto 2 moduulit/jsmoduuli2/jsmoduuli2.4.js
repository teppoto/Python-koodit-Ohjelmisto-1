const lista = []
let number = 1;

while (number !== 0){
  number =parseInt(prompt("Anna luku:"))
  lista.push(number)
}

lista.sort(function(a, b){return b - a});

for (let i = 0; i < lista.length; i++) {
  console.log(lista[i]);
}

