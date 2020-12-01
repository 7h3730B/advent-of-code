const fs = require('fs');
const { exit } = require('process');

let inputs = fs.readFileSync(__dirname + '/input.txt', { encoding: 'utf8', flag: 'r' }).split(',').map((input) => parseInt(input));

function getFirstValue(noun, verb, inputVec) {
    let inputs = inputVec.slice();
    inputs[1] = noun; inputs[2] = verb;
    let pc = 0;
    do {
        // Break if opcode = 99
        const opcode = inputs[pc];
        if (opcode === 99) {
            // console.log("exiting!");
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
    return inputs[0];
}

for (i = 0; i <= 99; i++) {
    for (j = 0; j <= 99; j++) {
        if (getFirstValue(i, j, inputs) == 19690720) {
            console.log(`The value is: ${100 * i + j}`); // 2552
        }
    }
}