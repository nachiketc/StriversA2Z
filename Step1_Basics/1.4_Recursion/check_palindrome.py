class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        string = []
        for i in range(len(s)):
            if s[i]>="A" and s[i]<="Z":
                string.append(s[i].lower())
            elif s[i]>="a" and s[i]<="z":
                string.append(s[i])
            elif s[i]>="0" and s[i]<="9":
                string.append(s[i])

        # print(string)
        if string==[]:
            return True

        return ( self.isPalindromeCheck(string))
    
    def isPalindromeCheck(self,listS):

        #base case
        # print(len(listS)==1)
        if len(listS)==1:
            return True
        elif len(listS)==2:
            if listS[-1]!=listS[0]:
                return False
            else:
                return True

        # print(listS)
        #thingstodo
        if listS[0]!=listS[-1]:
            return False

        #recursion call
        return self.isPalindromeCheck(listS[1:-1])