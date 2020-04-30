/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    let tracker = new Set();
    let answer = 0;
    let i = 0;
    let j = 0;
    while (i < s.length && j < s.length) {
        if (!tracker.has(s[j])) {
            tracker.add(s[j]);
            j++;
            answer = Math.max(answer, j - i);
        }
        else {
            tracker.delete(s[i]);
            i++;
        }
    }
    return answer;
};