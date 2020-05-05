/**
 * @param {number} x
 * @return {number}
 */
var reverse = function(x) {
    let signed;
    if (x < 0) {
        signed = true;
    }
    else {
        signed = false;
    }
    x = x.toString();
    if (signed) {
        x = x.substring(1);
    }
    x = x.split('');
    let i;
    let answer = "";
    for (i = x.length - 1; i >= 0; i--) {
        answer += x[i];
    }
    answer = parseInt(answer);
    if (signed) {
        answer = -answer;
    }
    if (answer > Math.pow(2, 31) - 1) {
        return 0
    }
    if (answer < Math.pow(-2, 31)) {
        return 0
    }
    return answer;
};