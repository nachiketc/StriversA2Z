class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        low,high = 0,len(nums)-1
        #find k
        k,lowVal,uppVal = -1,-1,-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]==target:
                return True
            #reduce array and check again
            if nums[mid]==nums[low]==nums[high]:
                low+=1
                high-=1
                continue
            elif nums[mid]==nums[low]:
                low+=1
                continue
            elif nums[high]==nums[mid]:
                high-=1
                continue

            #no duplicate on edges
            if nums[mid]>nums[low]:
                if nums[low]<=target<=nums[mid]:
                    high=mid-1
                else:
                    low=mid+1
            else:
                if nums[mid]<=target<=nums[high]:
                    low=mid+1
                else:
                    high=mid-1
            
        return False