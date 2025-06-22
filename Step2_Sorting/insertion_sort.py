class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # insertion sort

        # first loop through all elements

        for i in range(1,len(nums)):
            el = nums[i]

            # second loop through rest of the elements and insert into array[0,i-1]

            for j in range(0,i+1 ):

                # compare the with sorted array to insert

                if el < nums [j]:
                    nums[j], nums[j+1:i+1] = el ,  nums[j:i]
                    break
                


        return nums