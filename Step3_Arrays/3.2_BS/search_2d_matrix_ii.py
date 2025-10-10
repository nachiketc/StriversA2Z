class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:


        i,j = 0,0 # row and column index
        lowi,lowj = 0,0 #lower limit
        highi,highj = len(matrix)-1, len(matrix[0])-1 #upper limit

        #loop through row and columns of matrix
        while lowi<=highi and lowj<=highj :
            
            #bin search in every row 
            low,high=lowi,highi
            while low<=high:
                mid = low + (high-low)//2
                if matrix[mid][lowj]==target: #look for the element in lowj column amongst rows 
                    return True
                elif matrix[mid][lowj]<target and (mid==len(matrix)-1 or matrix[mid+1][lowj]>target): #if we find the edge row then we loop out
                    highi=mid
                    break
                elif matrix[mid][lowj]>target:
                    high=mid-1
                else:
                    low=mid+1

            #bin search in every column
            low,high=lowj,highj
            while low<=high:
                mid = low + (high-low)//2
                if matrix[lowi][mid]==target:
                    return True
                elif matrix[lowi][mid]<target and (mid==len(matrix[lowi])-1 or matrix[lowi][mid+1]>target):
                    highj=mid
                    break
                elif matrix[lowi][mid]>target:
                    high=mid-1
                else:
                    low=mid+1


            #increase lower limit of row and columns by 1
            lowi+=1
            lowj+=1
        return False
    
