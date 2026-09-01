class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int, p: int) -> int:
         n = len(nums)
         ans = 0

         for i in range(n - k + 1):
            subarray = nums[i:i + k]

            if len(set(subarray)) == k:
                ans = max(ans, sum(subarray))

         return ans