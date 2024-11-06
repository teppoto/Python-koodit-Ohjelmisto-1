function noppa(sivut) {
  let i = Math.floor(Math.random() * sivut) + 1;
  return i;
}

let heitto;

kysymys = parseInt(prompt("Nopan sivujen määrä"))
while (heitto !== kysymys) {
  heitto = noppa(kysymys);

  let li = document.createElement('li');
  li.textContent = heitto;
  document.querySelector('#target').appendChild(li);

  if (heitto === kysymys) {
    break;
  }
}