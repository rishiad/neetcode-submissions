class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        nums.sort()
        res = []
        
        for i, a in enumerate(nums):
            if a > 0:
                break

            if i > 0 and a == nums[i - 1]:
                continue
                
            l, r = i + 1, len(nums)-1
            while l < r:
                target = a + nums[l] + nums[r]
                if target == 0:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                elif target < 0:
                    l += 1
                elif target > 0:
                    r -= 1

        return res