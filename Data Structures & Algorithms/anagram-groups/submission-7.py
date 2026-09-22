from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sorted_strs = []
        # anagrams = []
        # visited = set()
        # for word in strs: 
        #     sorted_strs.append("".join(sorted(word)))

        # for i in range (len(sorted_strs)):
        #     if i not in visited:
        #         currentWord = sorted_strs[i]
        #         subList = [strs[i]]
                
        #         for j in range(i + 1, len(sorted_strs)):
        #             if sorted_strs[j] == currentWord:
        #                 subList.append(strs[j])
        #                 visited.add(j)
        #         anagrams.append(subList)
        
        # return anagrams

        # anagram_dict = {}
        # anagram = []

        # for word in strs: 
        #     sorted_word = "".join(sorted(word))
        #     if sorted_word not in anagram_dict: 
        #         anagram_dict[sorted_word] = [word]
        #     else:
        #         anagram_dict[sorted_word].append(word)

        
        # for key in anagram_dict:
        #     anagram.append(anagram_dict[key])
        
        # return anagram
        anagram_dict = defaultdict(list)

        for word in strs:
            letters = [0] * 26

            for char in word:
                letters[ord(char) - ord('a')] += 1
            
            anagram_dict[tuple(letters)].append(word)

        return list(anagram_dict.values())







        