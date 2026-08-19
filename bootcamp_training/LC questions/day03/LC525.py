#contiguous array
# class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count = 0 
        max_len = 0
        first_index = {0:-1}
        for i, num in enumerate(nums):
            if num == 1:
                count += 1
            else:
                count -= 1

            if count in first_index:
                max_len = max(max_len, i - first_index[count])
            else:
                first_index[count] = i
        return max_len
 