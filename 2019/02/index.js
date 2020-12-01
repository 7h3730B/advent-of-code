const fs = require('fs');
const { exit } = require('process');

let inputs = fs.readFileSync(__dirname + '/input.txt', { encoding: 'utf8', flag: 'r' }).split(',');
inputs = inputs.map((input) => parseInt(input));

// before running the program, replace position 1 with the value 12 and replace position 2 with the value 2.
inputs[1] = 12; inputs[2] = 2;

let pc = 0;
do {
    // Break if opcode = 99
    const opcode = inputs[pc];
    if (opcode === 99) {
        console.log("exiting!");
        break;
    }

    let pos1 = inputs[pc + 1];
    let pos2 = inputs[pc + 2];
    let pos3 = inputs[pc + 3];

    if (opcode === 1) {
        inputs[pos3] = inputs[pos1] + inputs[pos2];
    } else if (opcode === 2) {
        inputs[pos3] = inputs[pos1] * inputs[pos2];
    } else {
        console.log("Something went wrong!");
        break;
    }
    pc += 4;
} while (inputs.length >= pc);

console.log(`The value is: ${inputs[0]}`); // 9706670