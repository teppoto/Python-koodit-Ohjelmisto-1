const number1 = prompt("Anna kokonaisluku: ");
const number2 = prompt("Anna kokonaisluku: ");
const number3 = prompt("Anna kokonaisluku: ");

const number1s = parseInt(number1)
const number2s = parseInt(number2)
const number3s = parseInt(number3)


document.querySelector('#target').innerHTML += number1s + number2s + number3s;
document.querySelector('#target2').innerHTML += number1s * number2s * number3s;
document.querySelector('#target3').innerHTML += (number1s + number2s + number3s)/3;