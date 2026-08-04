#kids with the greatest number of candies
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans = []
        maximum = max(candies)
        for i in candies:
            ans.append(i + extraCandies >= maximum)
        return ans

        #time complexity = o(n)
        #space complexity = o(n)