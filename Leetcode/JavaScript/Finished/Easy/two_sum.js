/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */

let twoSum = function(nums, target) {
    let answers = {};
    let i;
    for (i = 0; i < nums.length; i++) {
        let difference = target - nums[i];
        if (nums[i] in answers) {
            return [answers[nums[i]], i];
        }
        else {
            answers[difference] = i;
        }
    }
};