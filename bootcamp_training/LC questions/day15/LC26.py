#permutation
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        current = []

        def backtrack():

            if len(current) == len(nums):
                ans.append(current.copy())
                return

            for num in nums:

                if num in current:
                    continue

                current.append(num)

                backtrack()

                current.pop()

        backtrack()

        return ans