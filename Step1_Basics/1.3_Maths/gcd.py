class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        smallest = 1001
        largest = -1
        for num in nums:
            if num>largest:
                largest=num
            if num<smallest:
                smallest=num

        print(smallest, largest)
        while largest!=0:
            smallest,largest = largest, smallest%largest
            print(smallest,largest)
            
        return smallest

        