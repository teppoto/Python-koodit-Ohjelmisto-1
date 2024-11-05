const neliöjuuri = confirm("Should I calculate the square root?")

if (neliöjuuri === true) {
  let numero = prompt("Give a number for square root: ")
  if (numero >= 0) {
    document.querySelector('#target').innerHTML = "The square root is:" + Math.sqrt(numero)
  } else if (numero <= 0) {
    document.querySelector('#target').innerHTML = "The square root of a negative number is not defined";
  }
} else {
  document.querySelector('#target').innerHTML = "The square root is not calculated.";
}