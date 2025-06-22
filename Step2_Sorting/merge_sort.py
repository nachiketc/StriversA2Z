class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # merge sort
        self.merge_sort(nums,0,len(nums)-1)
        return nums
    
    def merge_sort(self,nums:List[int],n1:int,n2:int):
        mid = (n1+n2)//2
        if n2>n1:
            # print("merge_sort -call ",nums,n1,(n1+n2)//2,((n1+n2)//2)+1,n2)

            self.merge_sort(nums,n1,mid)
            self.merge_sort(nums,mid+1,n2)
            self.merge(nums,n1,mid,mid+1,n2)


    
    def merge(self,nums:List[int],n1:int,n2:int,l1:int,l2:int):
        # print("merge-call",nums,nums[n1:l2+1],nums[n1:n2+1],nums[l1:l2+1])
        num=[0]*(l2-n1+1)
        i,j,p=n1,l1,0
        while i<=n2 and j<=l2:
            # print(nums,nums[n1:l2+1],nums[n1:n2+1],nums[l1:l2+1])
            if nums[i]<=nums[j]:
                num[p] = nums[i]
                i+=1
            else:
                num[p] = nums[j]
                j+=1
            p+=1
        
            # if nums[i]<=nums[j]: #no swap
            #     nums[p]=nums[i]
            #     i+=1
            # else :
            #     nums[p],nums[i+1:nn+2] = nums[j],nums[i:nn+1]
            #     i+=1
            #     j+=1
            #     nn+=1 lshw -C multimedia
            # p+=1
        
        if i<=n2:
            num[p:]=nums[i:n2+1]
        elif j<=l2:
            num[p:]=nums[j:l2+1]
        
        nums[n1:l2+1]=num
        # print(nums,nums[n1:l2+1],nums[n1:n2+1],nums[l1:l2+1])


            