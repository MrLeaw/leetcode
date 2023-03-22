class Solution:
    def findLucky(self, arr: List[int]) -> int:
        vals=[0]*(max(arr)+1)
        for elem in arr:
            vals[elem]+=1
        o=-1
        for i in range(len(vals)):
            if i == vals[i] and i != 0:
                if i>o:
                    o=i
        return o