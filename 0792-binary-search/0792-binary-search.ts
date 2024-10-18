function search(nums: number[], target: number): number {
    let start = 0,
        end = nums.length - 1
    while (start <= end) {
        let m = Math.round((start + end) / 2)
        // console.log(`start ${start} , end ${end},m ${m} , mus[m]: ${nums[m]}`)
        if (nums[m] > target) {
            end = m - 1

        } else if (nums[m] < target) {
            start = m + 1
        } else return m
    }
    return -1

};