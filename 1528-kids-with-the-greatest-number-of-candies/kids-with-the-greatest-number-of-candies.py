class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        result=[]
        n=len(candies)
        mm=max(candies)
        for i in range(0,n):
            candies[i]<=mm
            if candies[i]+extraCandies>=mm:
                result.append(True)
            else:
                result.append(False)
        return result
