const vuosiluku = prompt("Anna kokonaisluku: ");

if (vuosiluku % 4 == 0) {
  if (vuosiluku % 400 == 0) {
    document.querySelector('#target').innerHTML = "on karkausvuosi";
  } else if (vuosiluku % 100 == 0) {
    document.querySelector('#target').innerHTML = "ei ole karkausvuosi";
  } else {
    document.querySelector('#target').innerHTML = "on karkausvuosi";
  }
}
else {
    document.querySelector('#target').innerHTML = "ei ole karkausvuosi";}