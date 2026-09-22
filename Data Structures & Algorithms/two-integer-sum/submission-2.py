class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # sort -> two pointers -> slide left and right dependsing on the conditions 
        # nums.sort()
        # i, j = 0, len(nums) - 1
        # while i != j: 
        #     if nums[i] + nums[j] == target:
        #         return [i, j]
        #     elif nums[i] + nums[j] > target:
        #         j -= 1
        #     else: 
        #         i += 1
        for i in range(len(nums)):
            for j in range (i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        
        