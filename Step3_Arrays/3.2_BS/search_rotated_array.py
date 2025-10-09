class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low,high = 0,len(nums)-1
        #find k
        k,lowVal,uppVal = -1,-1,-1
        while low<=high:
            mid=(low+high)//2
            if mid==len(nums)-1:
                break
            else :
                if ((mid<len(nums)-1) and nums[mid]>nums[mid+1]):
                    k=mid
                    lowVal=nums[mid+1]
                    uppVal=nums[mid]
                    break
                elif nums[mid]>nums[-1]:
                    low=mid+1
                else:
                    high=mid-1

        # print(k,lowVal,uppVal)
        if k==-1:
            return self.binarySearch(nums,target,0)
        else:
            if target == nums[0]:
                return 0
            elif target < nums[0]:
                return self.binarySearch(nums[k+1:],target,k+1)
            else:
                return self.binarySearch(nums[:k+1],target,0)

    
    def binarySearch(self, nums: List[int], target: int, startIndex:int) -> int:
        print(nums,target)
        low,high = 0,len(nums)-1
        while low<=high:
            mid = (low+high)//2
            if nums[mid] == target:
                return mid+startIndex
            elif nums[mid]>target:
                high=mid-1
            else:
                low=mid+1
        return -1