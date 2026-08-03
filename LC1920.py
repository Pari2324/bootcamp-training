#build array from permutation
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            ans.append(nums[nums[i]])
        return ans
        #time complexity = o(n)
        #space complexity = o(n)