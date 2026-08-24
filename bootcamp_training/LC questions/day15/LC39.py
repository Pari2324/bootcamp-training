#combination sum
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        current = []

        def backtrack(start, remaining):

            if remaining == 0:
                ans.append(current.copy())
                return

            if remaining < 0:
                return

            for i in range(start, len(candidates)):

                current.append(candidates[i])

                backtrack(i, remaining - candidates[i])

                current.pop()

        backtrack(0, target)

        return ans