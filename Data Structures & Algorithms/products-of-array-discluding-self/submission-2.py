class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        product = 1

        # for i in range(len(nums)):
        #     product = 1
            
        #     for j in range(len(nums)):
        #         if i != j:
        #             product *= nums[j]

        #     result.append(product)

        for n in nums:
            product *= n

        for i in range(len(nums)):
            if nums[i] == 0:
                zero_product = 1
                for j in range(len(nums)):
                    if i != j:
                        zero_product *= nums[j]
                result.append(zero_product)
            else: 
                result.append(product//nums[i])
        
        return result
            
        