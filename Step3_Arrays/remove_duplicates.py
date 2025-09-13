class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        last = -101
        
        # rearrange the array using 2 pointer
        i,j = 0,1
        count=1
        while i<j and j<len(nums): # check conditions
            if nums[i]==nums[j]:
                j+=1
            else:
                #unique element
                count+=1
                #swap
                i+=1
                nums[i]=nums[j]
                j+=1
        return count