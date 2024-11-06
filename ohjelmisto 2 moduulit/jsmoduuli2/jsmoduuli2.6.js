function noppa() {
  let i = Math.floor(Math.random() * 6) + 1;
  return i;
}

let heitto;

while (true) {
  heitto = noppa();

  let li = document.createElement('li');
  li.textContent = heitto;
  document.querySelector('#target').appendChild(li);

  if (heitto === 6) {
    break;
  }
}