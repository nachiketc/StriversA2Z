class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        kk = k%n
        # print(n,k,k%n)
        # print(nums[n-kk:]+nums[:n-kk])
        nums[:kk], nums[kk :] = nums[n-kk:],nums[:n-kk]
        # print(nums)
