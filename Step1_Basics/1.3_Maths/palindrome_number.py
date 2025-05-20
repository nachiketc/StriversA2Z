class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        num=x
        reverseNum=0
        while num>=1:
            digit = num%10
            reverseNum = reverseNum*10 + digit
            num = num/10
        return reverseNum==x
        