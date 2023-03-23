class Solution:
    def longestCommonPrefix(self,strs) -> str:
        if len(strs)==0:
            return ""
        if len(strs)==1:
            return strs[0]
        
        l = []
        for elem in strs:
            l.append(len(elem))
        m=min(l)
        s=True
        
        if min(l)==0:
            return ""
        
        for i in range(m):
            p=strs[0][i]
            for e in strs:
                if not e[i] ==p:
                    s=False
                    return strs[0][0:i]
                p=e[i]
        return strs[0][0:m]