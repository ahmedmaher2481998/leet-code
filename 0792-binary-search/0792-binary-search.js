/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function (nums, target) {
    let start = 0,
        end = nums.length - 1
    while (start <= end) {
        m = Math.round((start + end) / 2)
        if (nums[m] > target) end = m - 1
        else if (nums[m] < target) start = m + 1 
        else return m 
    }
return -1
    
};