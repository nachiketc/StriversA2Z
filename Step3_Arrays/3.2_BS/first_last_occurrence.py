class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        #upper bound search
        uppBound = -1
        low,high = 0,len(nums)-1
        while low<=high:
            mid = (low+high)//2
            # print(low,mid,high)
            if (nums[mid]==target and 
                ((mid<len(nums)-1 and nums[mid+1]>target) or (mid == len(nums)-1))):
                uppBound = mid
                break
            elif nums[mid]<target:
                low=mid+1
            elif nums[mid]>target:
                high=mid-1
            else:
                low=mid+1
        
        #lower bound search
        lowBound = -1
        low,high = 0,len(nums)-1
        while low<=high:
            mid = (low+high)//2
            if (nums[mid]==target and 
                ((mid>0 and nums[mid-1]<target) or (mid == 0))):
                lowBound = mid
                break
            elif nums[mid]<target:
                low=mid+1
            elif nums[mid]>target:
                high=mid-1
            else:
                high=mid-1
        
        return [lowBound,uppBound]

