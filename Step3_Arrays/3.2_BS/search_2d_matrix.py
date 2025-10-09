class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #find the row
        rowLastIndex = len(matrix[0])-1
        low,high = 0, len(matrix)-1
        # rowVal=-1
        while (low<=high):
            mid = low + (high-low)//2
            # print(low,mid,high,matrix[mid],target,matrix[mid][0],matrix[mid][rowLastIndex],matrix[mid][0]>=target and matrix[mid][rowLastIndex]<=target)
            if matrix[mid][0]<=target and matrix[mid][rowLastIndex]>=target:
                return self.binS(matrix[mid],target)
            elif matrix[mid][0]>target:
                high=mid-1
            else:
                low=mid+1
        return False

    def binS(self, nums: List[int],target:int) -> bool:
        print(nums,target)
        low,high = 0, len(nums)-1
        while low<=high:
            mid = low + (high-low)//2
            if nums[mid]==target:
                return True
            elif nums[mid]>target:
                high=mid-1
            else : 
                low=mid+1
        return False