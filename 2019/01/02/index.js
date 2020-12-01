const fs = require('fs');

function fuelCalcualtion(mass) {
    return (Math.floor(mass / 3)) - 2;
}

let requiredFuel = 0;

fs.readFileSync(__dirname + '/input.txt', { encoding: 'utf8', flag: 'r' }).split('\n').forEach((mass) => {
    let fuelValues = [];
    while (fuelCalcualtion(mass) > 0) {
        fuelValues.push(fuelCalcualtion(mass));
        mass = fuelValues[fuelValues.length - 1];
    }
    fuelValues.forEach((f) => {
        requiredFuel += f;
    });
});

console.log(`The Fuel needed is: ${requiredFuel}`); // => 5057481