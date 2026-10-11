class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # if not nums:
        #     return 0

        # nums.sort()
        # current, largest = 1, 1

        # for i in range (1, len(nums)):
        #     if nums[i] == nums[i - 1]:
        #         continue
        #     elif nums[i] - nums[i-1] == 1:
        #         current += 1
        #         largest = max(current, largest)
        #     else:
        #         current = 1
        
        # return largest

        num_set = set(nums)

        largest = 0

        for n in nums:
            if n-1 not in num_set:
                length = 1
                while(n + length) in num_set:
                    length += 1
                largest = max(length, largest)
        
        return largest