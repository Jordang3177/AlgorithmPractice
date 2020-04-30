'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.replace(/\s*$/, '')
        .split('\n')
        .map(str => str.replace(/\s*$/, ''));

    main();
});

function readLine() {
    return inputString[currentLine++];
}

// Complete the minimumBribes function below.
function minimumBribes(q) {
    let answer = 0;
    var i;
    for (i = q.length - 1; i >= 0; i--) {
        if (q[i] == i + 1) {
            continue;
        }
        else if(q[i - 1] == i + 1) {
            let a,b;
            a = q[i];
            b = q[i - 1];
            q[i] = b;
            q[i - 1] = a;
            answer += 1;
        }
        else if(q[i - 2] == i + 1) {
            let a,b,c;
            a = q[i];
            b = q[i - 1];
            c = q[i - 2];
            q[i] = c;
            q[i - 1] = a;
            q[i - 2] = b;
            answer += 2;
        }
        else {
            return "Too chaotic";
        }
    }
    return answer;
}

function main() {
    const t = parseInt(readLine(), 10);

    for (let tItr = 0; tItr < t; tItr++) {
        const n = parseInt(readLine(), 10);

        const q = readLine().split(' ').map(qTemp => parseInt(qTemp, 10));

        const result = minimumBribes(q);

        console.log(result);
    }
}
