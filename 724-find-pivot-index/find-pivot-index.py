class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total=sum(nums)
        sumleft=1-1
        n=len(nums)
        for i in range(0,n):
            sumright = total-sumleft-nums[i]
            if sumleft==sumright:
                return i
            sumleft=sumleft+nums[i]
        return -1
