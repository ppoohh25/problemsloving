class Solution:
    def removeElement(self, nums: List, val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] = 555
        nums.sort()
        for i in range(len(nums)):
            if nums[i] != 555:
                k+=1
        return k