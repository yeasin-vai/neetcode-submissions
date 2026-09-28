class Solution:

    def encode(self, strs: List[str]) -> str:
        resp = ''
        for s in strs: 
            resp += str(len(s)) + '#' + s
        return resp


    def decode(self, s: str) -> List[str]:
        # print(s)
        # if not s:
        #     print('early')
        #     return []
        # else:
        #     print('late')
        #     return s.split('🚀')
        arr,i = [],0
        print(s)

        while (i < len(s)):
            j = i
            print(i,j)
            while s[j] != '#':
                j += 1
            print(j)
            length = int(s[i: j])
            print(length)
            arr.append(s[j+1 : j + length+1])
            print(s[j+1 : j + length + 1])
            i = j + length + 1
        
        
        return arr



