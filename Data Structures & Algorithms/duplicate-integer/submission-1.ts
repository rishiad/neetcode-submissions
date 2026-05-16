class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums: number[]): boolean {
        let seen_set = new Set()

        for (let i = 0; i < nums.length; i++) {
            if (seen_set.has(nums[i])) {
                return true
            }
            seen_set.add(nums[i])
        }

        return false
    }
}
