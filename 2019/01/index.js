const fs = require("fs");

let completeFuelLevel = 0;

fs.readFileSync(__dirname + '/input.txt', { encoding: 'utf8', flag: 'r' }).split("\n").forEach((mass) => {
    completeFuelLevel += (Math.floor(mass / 3)) - 2;
});

console.log(`The Fuel needed is: ${completeFuelLevel}`); // => 3373568