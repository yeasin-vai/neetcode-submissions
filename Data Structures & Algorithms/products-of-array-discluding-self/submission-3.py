class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        product = 1
        z = 0

        # for i in range(len(nums)):
        #     product = 1
            
        #     for j in range(len(nums)):
        #         if i != j:
        #             product *= nums[j]

        #     result.append(product)

        # for n in nums:
        #     product *= n

        # for i in range(len(nums)):
        #     if nums[i] == 0:
        #         zero_product = 1
        #         for j in range(len(nums)):
        #             if i != j:
        #                 zero_product *= nums[j]
        #         result.append(zero_product)
        #     else: 
        #         result.append(product//nums[i])

        for n in nums: 
            if n : 
                product *= n
            else: 
                z += 1
        
        if z > 1 : return result

        for i, n in enumerate(nums): 
            if z : 
                if n: 
                    result[i] = 0
                else: 
                    result[i] = product
            else: 
                result[i] = product // n

        # 1, 1, 2, 8 - 1, 6, 24, 48
        
        return result
            
        