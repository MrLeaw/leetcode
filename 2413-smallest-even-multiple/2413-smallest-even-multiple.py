class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        m1,m2=[],[]
        n1,n2=0,0
        while True:
            n1+=2
            n2+=n
            m1.append(n1)
            m2.append(n2)
            for a in m1:
                for b in m2:
                    if a == b and a%2==0:
                        return a