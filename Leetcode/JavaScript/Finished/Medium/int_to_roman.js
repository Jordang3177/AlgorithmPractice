/**
 * @param {number} num
 * @return {string}
 */
var intToRoman = function(num) {
    let answer = [];
    while (num !== 0) {
        if (num >= 1000) {
            answer.push('M');
            num -= 1000;
        }
        else if (num >= 900) {
            answer.push('CM');
            num -= 900;
        }
        else if (num >= 500) {
            answer.push('D');
            num -= 500;
        }
        else if (num >= 400) {
            answer.push('CD');
            num -= 400;
        }
        else if (num >= 100) {
            answer.push('C');
            num -= 100;
        }
        else if (num >= 90) {
            answer.push('XC');
            num -= 90;
        }
        else if (num >= 50) {
            answer.push('L');
            num -= 50;
        }
        else if (num >= 40) {
            answer.push('XL');
            num -= 40;
        }
        else if (num >= 10) {
            answer.push('X');
            num -= 10;
        }
        else if (num >= 9) {
            answer.push('IX');
            num -= 9;
        }
        else if (num >= 5) {
            answer.push('V');
            num -= 5;
        }
        else if (num >= 4) {
            answer.push('IV');
            num -= 4;
        }
        else {
            answer.push('I');
            num -= 1;
        }
    }
    return answer.join('');
};