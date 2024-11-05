const nimi = prompt("Anna nimi: ")
const lista = ['Gryffindor', 'Slytherin', 'Hufflepuff', 'Ravenclaw']

valinta = Math.floor(Math.random() * lista.length)

document.querySelector('#target').innerHTML = nimi + " you are a " + lista[valinta]



