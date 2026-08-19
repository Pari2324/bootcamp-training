# subarrays sum divisible by k
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        remainder = [0]*k
        remainder[0] = 1
        prefix_sum = 0
        count = 0
        for num in nums:
            prefix_sum += num
            rem = prefix_sum % k
            count += remainder[rem]
            remainder[rem] += 1
        return count

        