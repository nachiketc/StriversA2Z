class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        #bubble sort

        #first loop all the way
        for i in range(len(nums)):
            # second loop decreasing limit
            for j in range(0,len(nums)-i-1):
                # temp2 = nums[j]
                if nums[j]>nums[j+1]:
                    # swap
                    temp = nums[j]
                    nums[j] = nums[j+1]
                    nums[j+1] = temp
        return nums