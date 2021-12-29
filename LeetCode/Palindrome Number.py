class Solution:
    def isPalindrome(self, x: int) -> bool:
        sx = str(x)
        a = []
        for i in range(len(sx)):
            a.append(sx[i])
        if a == a[::-1]:
            ans = True
        else:
            ans = False
        return ans