class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
          low,high = 0, len(nums)-1
          if high==0:
            return 0
          else :  
            while (low<=high):
                mid = low + (high-low)//2
                # print(low,mid,high)
                # print(nums[low],nums[mid],nums[high])
            # check for beginning and  end
                #beginning
                if (mid==0 and nums[mid]>nums[mid+1]):
                    return 0
                #end 
                if (mid==len(nums)-1 and nums[mid-1]<nums[mid]):
                    return mid
            # check for anything in the middle
                # print(mid-1,mid,mid+1,nums[mid-1],nums[mid],nums[mid+1])
                if (nums[mid-1]<nums[mid]) and (nums[mid+1]<nums[mid]):
                    return mid
                elif (nums[mid-1]>nums[mid] and nums[mid]>nums[mid+1]):
                    high=mid-1
                elif nums[mid-1]<nums[mid] and nums[mid]<nums[mid+1] :
                    low=mid+1
                elif (nums[mid-1]>nums[mid+1]):
                    high=mid-1
                else:
                    low=mid+1