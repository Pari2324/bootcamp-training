# product of array except self
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
        leftproduct = 1
        for i in range(len(nums)):
            ans[i] = leftproduct 
            leftproduct *= nums[i]
        rightproduct = 1
        for i in range(len(nums) -1, -1, -1):
            ans[i] *= rightproduct
            rightproduct *= nums[i]
        return ans
