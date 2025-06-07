class Solution:
    def isHappy(self, n: int) -> bool:
        setNum = set()
        while (n != 1) and (n not in setNum):
            setNum.add(n)
            n=self.compute(n)
            # print(n)

        if n in setNum:
            return False
        elif n==1:
            return True


    def compute(self,n: int ) -> int:
        digits = [int(d) for d in str(n)]
        return sum([d**2 for d in digits])

    # not technically hashmap problem but a simple set storage problem