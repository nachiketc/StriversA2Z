class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        setNum= set()
        for num in nums:
            if num in setNum:
                return True
            else:
                setNum.add(num)

        return False