from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occurance = defaultdict(list)

        for i in range(len(nums)): 
            occurance[nums[i]].append(i)
        
        sorted_pos = sorted(occurance.values(), key=lambda x: len(x))
        # [2,4,2,4,2,3,4,4,2,1]
        # 1 -> [0], 2 ->         
        # result = []
        # x = len(sorted_pos)
        # for j in range(x -1, x-k-1, -1): 
        #     print(x, k, x -1, x-k)
        #     result.append(nums[sorted_pos[j][0]])
        #     print('run')
        
        # return result

        result = []

        for srt_pos in sorted_pos[-k:]:
            result.append(nums[srt_pos[0]])
        return result



        