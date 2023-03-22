class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        res=0
        if s[0]=="-":
            res= -int(s[::-1].replace("-",""))
        else:
            res= int(s[::-1])
        if abs(res) > pow(2,31):
            return 0
        return res