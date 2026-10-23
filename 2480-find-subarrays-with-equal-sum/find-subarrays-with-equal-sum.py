class Solution(object):
    def findSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen=set()
        for i in range(len(nums)-1):
            smpair= nums[i]+nums[i+1]
            if smpair in seen:
                return True
            seen.add(smpair)       
        return False

