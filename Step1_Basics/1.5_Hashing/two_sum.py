class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #we know the target so we store key, value as key, target-key and then check for existence of value in the dictionary
        #wrong approach we need to store indices because we need to returb then
        # key, value = key, index of key
        diffL = defaultdict(list)
        for i in range(len(nums)):
            diffL[nums[i]].append(i)
        
        for num in nums:
            diff = target - num 
            if diff == num:
                if len(diffL[num])>=2:
                    return diffL[num][:2]
            elif diffL[diff] != [] and diffL[diff] != diffL[num] :
                return [diffL[num][0],diffL[diff][0]]
        

