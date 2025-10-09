class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        #we need to play with indices
        low,high = 0,len(nums)-1
        if len(nums)==1:
            return nums[0]
        while low<=high:
            mid = (low+high)//2
            # print(low,high,mid)
            isOdd = mid%2
            if isOdd: #target cannot be at odd place so we just traverse
                if nums[mid]==nums[mid-1]:
                    low=mid+1
                elif nums[mid]==nums[mid+1]:
                    high=mid-1
                
            else: #target is definitely at even place
                #check for first index
                if mid==0:
                    if nums[mid]!=nums[mid+1]:
                        return nums[mid]
                    else:
                        low=mid+2
                elif mid==len(nums)-1:
                    if nums[mid]!=nums[mid-1]:
                        return nums[mid]
                    else:
                        high=mid-2
                else:
                    if nums[mid]!=nums[mid-1] and nums[mid]!=nums[mid+1]:
                        return nums[mid]
                    elif nums[mid]==nums[mid-1]:
                        high=mid-1
                    else:
                        low=mid+1

