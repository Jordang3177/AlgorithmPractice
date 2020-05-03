/**
 * @param {string} J
 * @param {string} S
 * @return {number}
 */
var numJewelsInStones = function(J, S) {
    let i;
    let answer = 0;
    for (i = 0; i < J.length; i++) {
        answer += S.split(J[i]).length - 1;
    }
    return answer

};