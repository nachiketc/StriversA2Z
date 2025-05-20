class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        xm = abs(x)
        num = 0
        while xm>=1:
            digit = xm%10
            num=num*10 + digit 
            xm/=10
        if num>2**31-1 or num<-2**31:
            return 0
        return num if x>0 else (-1*num)