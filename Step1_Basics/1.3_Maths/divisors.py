#User function Template for python3

class Solution:
    def print_divisors(self, N):
        # code here
        divisors=[]
        for i in range(1,int(N**0.5)+1):
            if N%i==0:
                divisors.append(i)
                if i != N//i:
                    divisors.append(N//i)
                    
        divisors.sort()
        print(divisors)