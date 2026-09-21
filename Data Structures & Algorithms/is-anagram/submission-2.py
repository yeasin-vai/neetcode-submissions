class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
            
        s_dict = {}
        t_dict = {}

        for n in s:
            if n in s_dict:
                s_dict[n] += 1
            else:
                s_dict[n] = 0
        
        for n in t:
            if n in t_dict:
                t_dict[n] += 1
            else:
                t_dict[n] = 0

        for key in s_dict:
            if key not in t_dict:
                return False
            if s_dict[key] != t_dict[key]:
                return False
        return True
        