'use strict';
const names = ['John', 'Paul', 'Jones'];

let target = document.getElementById('target')

names.forEach(name => {
  let li = document.createElement('li')
  li.textContent = name
  target.appendChild(li)
})