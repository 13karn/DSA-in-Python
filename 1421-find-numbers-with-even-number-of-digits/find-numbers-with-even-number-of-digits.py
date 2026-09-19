class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        answer=0
        for number in nums:
            count=0 
            while number!=0:
                number= number//10
                count += 1
            if count%2==0:
                answer+=1
        return answer

        