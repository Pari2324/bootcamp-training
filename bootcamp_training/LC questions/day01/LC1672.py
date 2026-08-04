# richest customer wealth
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        for customer in accounts:
            current = 0
            for money in customer:
                current += money
            max_wealth = max(current,max_wealth)
        return max_wealth

        #time complexity = o(nxm)
        #space complexity = o(1)