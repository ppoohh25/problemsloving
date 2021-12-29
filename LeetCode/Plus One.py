class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = ''
        a =[]
        for i in range(len(digits)):
            n += str(digits[i])
        n = int(n)+1
        ans = str(n)
        for i in range(len(ans)):
            a.append(ans[i])
        return a