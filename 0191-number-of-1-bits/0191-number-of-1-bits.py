class Solution:
    def hammingWeight(self, n: int) -> int:
        n = int(bin(n)[2:])
        li = []

        if n // 10 or n == 1:
            li.append(1)

        while n // 10:
            if n % 10 == 1:
                li.append(n % 10)
            n = n // 10
        
        return len(li)
