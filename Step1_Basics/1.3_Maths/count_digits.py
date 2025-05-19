class Solution:
    def countDigit(self, n):
        count=0
        while n>=1:
            n=n/10
            count+=1
        return count