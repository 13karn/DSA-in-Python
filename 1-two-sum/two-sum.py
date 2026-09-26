class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n= len(nums)
      
        dictnry= {}
        for i in range(0,n):
            remaining = target-nums[i]
            if remaining in dictnry:
              return [dictnry[remaining],i]
            dictnry[nums[i]] = i
      