class Solution:
    def reverseBits(self, n: int) -> int:
        reversed = 0
        for _ in range(32):
            reversed <<= 1
            if n & 1:
                reversed += 1
            n >>= 1

        return reversed
