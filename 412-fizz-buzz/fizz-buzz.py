class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        madhav = []
        for i in range(1,n+1):
             if i% 3==0 and i%5==0 :
                 madhav.append("FizzBuzz")
             elif i%3==0:
                 madhav.append("Fizz")
             elif i%5==0:
                 madhav.append("Buzz")
             else :
                 madhav.append(str(i))
        return madhav