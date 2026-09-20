class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans=[]
        n=len(nums)
        for i in range(0,n):
            calc= nums[nums[i]]
            ans.append(calc)
        return ans