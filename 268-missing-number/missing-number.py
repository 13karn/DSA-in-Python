class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n= len(nums)
        exsum= n*(n+1) //2
        acsum= sum(nums)
        return exsum-acsum