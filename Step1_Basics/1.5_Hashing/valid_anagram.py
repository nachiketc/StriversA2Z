class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        slist = defaultdict(int)
        tlist = defaultdict(int)
        for ch in s:
            slist[ch]+=1
        
        for ch in t:
            tlist[ch]+=1
        
        return slist==tlist