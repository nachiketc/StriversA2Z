class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j=0
        swapCount=0
        ##space efficient solution i -> non zero index; j-> checking index
        # #full swap
        # while j<len(nums)-1-swapCount  :
        #     if nums[j]==0:
        #         #swap
        #         nums[j:len(nums)-1],nums[-1] = nums[j+1:],0
        #         swapCount+=1
        #     else:
        #         j+=1
        
        i=0
        #immediate swap
        for j in range(len(nums)):
            if nums[j]!=0:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
            

        ##time efficient solution - doesnt work 
        # nums1 = []
        # count = 0
        # for i in range(len(nums)):
        #     if nums[i]!=0:
        #         nums1.append(nums[i])
        #     else:
        #         count+=1
        # nums1.extend([0]*count)
        # print(nums1)
        # nums[:]=nums1
        