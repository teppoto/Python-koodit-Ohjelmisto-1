const luvut = [];

for (var i = 0; i < 5; i++) {
   luvut.push(prompt("Enter a number"));
}

for (let i = luvut.length - 1; i >= 0; i--) {
     console.log(`Number: ${luvut[i]}`);
}