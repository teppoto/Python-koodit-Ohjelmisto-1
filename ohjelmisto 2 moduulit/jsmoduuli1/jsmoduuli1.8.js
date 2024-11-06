const startYear = parseInt(prompt("Enter the start year: "));
const endYear = parseInt(prompt("Enter the end year: "));

const target = document.querySelector('#target');

const ul = document.createElement('ul');

for (let year = startYear; year <= endYear; year++) {
  if ((year % 4 === 0 && year % 100 !== 0) || (year % 400 === 0)) {
    const li = document.createElement('li');
    li.textContent = year;
    ul.appendChild(li);
  }
}

target.innerHTML = "";
target.appendChild(ul);