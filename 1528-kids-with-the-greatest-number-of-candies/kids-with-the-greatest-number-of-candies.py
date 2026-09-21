class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        result=[]
        n=len(candies)
        m=max(candies)
        for i in range(0,n):
            candies[i]<=m
            if candies[i]+extraCandies>=m:
                result.append(True)
            else:
                result.append(False)
        return result
