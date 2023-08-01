class Solution:
    def reverseBits(self, n: int) -> int:
        b = 0
        counter = 32
        while counter:
            if n & 1:
                b = b << 1
                b += 1
            else:
                b = b << 1
            n = n >> 1
            counter -= 1
        return b
