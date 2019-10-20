
class Solution(object):
    def bitmap(self, n):
        bm = [0] * 10000000

        for i in range(len(n)):
            bm[int(n[i].strip())] = 1
        return bm


f = open("numbers.txt", "r")
t1 = Solution()
t1.bitmap(f.readlines())
