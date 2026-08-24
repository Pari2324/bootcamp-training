#subsets
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        current = []

        def backtrack(start):

            ans.append(current.copy())

            for i in range(start, len(nums)):

                current.append(nums[i])

                backtrack(i + 1)

                current.pop()

        backtrack(0)

        return ans
        