class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # mm,i,j = m,0,0
        # while i<mm and j<n:
        #     if nums2[j]<=nums1[i]:
        #         nums1[i],nums1[i+1:] = nums2[j],nums1[i:m+n-1]
        #         j+=1
        #         i+=1
        #         mm+=1
        #     else:
        #         i+=1
        #     # print(nums1,nums2,i,j)
        # if j<n:
        #     nums1[i:] = nums2[j:]
        #     # print(nums1,nums2,i,j)

        i,j,p = m-1,n-1,m+n-1
        while i>=0 and j>=0:
            if nums1[i]>nums2[j]:
                nums1[p] = nums1[i]
                i-=1
            else:
                nums1[p] = nums2[j]
                j-=1
            p-=1
            # print(nums1,nums2,i,j,p)
            
        if j>=0:
            # print(nums1,nums2,i,j,p)

            nums1[:j+1] = nums2[:j+1]