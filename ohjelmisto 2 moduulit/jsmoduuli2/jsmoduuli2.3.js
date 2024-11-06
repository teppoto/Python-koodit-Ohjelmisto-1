let olista = []

for (let i = 0; i < 6; i++) {
  olista.push(prompt("Anna osallistuja nimi: "))
}

olista.reverse();

olista.forEach(name => {
  let li = document.createElement('li');
  li.textContent = name;
  document.querySelector('#target').appendChild(li);
});
