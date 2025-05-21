#User function Template for python3

class Solution:
    def armstrongNumber (self, n):
        # code here 
        digits=[]
        count=0
        num=n
        while num>=1:
            digits.append(num%10)
            count+=1
            num=num//10
        
        result=0
        for digit in digits:
            result+= digit**count
        
        # print(result,digits, count, n)
        
        return result==n