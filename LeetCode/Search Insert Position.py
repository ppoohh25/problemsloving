class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        a = []
        if target > nums[0] :
            for i in range(len(nums)):
                if target >= nums[i]:
                    a.append(i)
            if target == nums[max(a)]:
                return max(a)
            else:
                return max(a)+1
        if target <= nums[0]:
            a.append(str(0))
            return ''.join(a)