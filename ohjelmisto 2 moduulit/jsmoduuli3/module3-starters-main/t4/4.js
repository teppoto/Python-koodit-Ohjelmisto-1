'use strict';
const students = [
  {
    name: 'John',
    id: '2345768',
  },
  {
    name: 'Paul',
    id: '2134657',
  },
  {
    name: 'Jones',
    id: '5423679',
  },
];

let target = document.getElementById('target')

students.forEach(student => {
  let option = document.createElement('option')
  option.value = student.id
  option.textContent = student.name
  target.appendChild(option)
})