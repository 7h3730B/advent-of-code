const fs = require("fs");

function calcuteFuelForMassOfOneModule (mass) {
    // dividy mass by three than round it down and subtract 2
    return (Math.floor(mass / 3)) - 2;
}

const input_modules_mass = fs.readFileSync(__dirname + '/input.txt', { encoding:'utf8', flag: 'r' });

let completeFuelLevel = 0;

input_modules_mass.split("\n").forEach( (mass) => {
    completeFuelLevel += calcuteFuelForMassOfOneModule(mass);
});

console.log(`The Fuel needed is: ${completeFuelLevel}`);