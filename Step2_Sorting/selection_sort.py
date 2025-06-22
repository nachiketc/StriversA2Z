class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # selection sort

        # First loop though all elements and sort that index with ith smallest
        for i in range(len(nums)):
            min = nums[i]
            index = i
            for j in range(i+1,len(nums)):
                if min>nums[j]:
                    min = nums[j]
                    index = j
            # swap
            temp = nums[index]
            nums[index] = nums[i]
            nums[i] = temp

        return nums