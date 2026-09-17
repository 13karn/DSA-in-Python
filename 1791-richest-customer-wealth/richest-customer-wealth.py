class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        maximum = 0
        for i in range(len(accounts)):
            a = sum(accounts[i])
            if a>maximum:
                maximum = a 
        return maximum