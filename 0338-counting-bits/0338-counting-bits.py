class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0]

        for i in range(n):
            bNum = i + 1
            bits = 0
            while bNum:
                bNum &= bNum - 1
                bits += 1
            ans.append(bits)

        return ans
