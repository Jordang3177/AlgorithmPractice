/**
 * @param {string} ransomNote
 * @param {string} magazine
 * @return {boolean}
 */
var canConstruct = function (ransomNote, magazine) {
  let dictionary = {};
  let char;
  for (char of magazine) {
    if (dictionary[char] !== undefined) {
      dictionary[char] += 1;
    } else {
      dictionary[char] = 1;
    }
  }
  for (char of ransomNote) {
    if (dictionary[char] !== undefined) {
      dictionary[char] -= 1;
      if (dictionary[char] < 0) {
        return false;
      }
    } else {
      return false;
    }
  }
  return true;
};
