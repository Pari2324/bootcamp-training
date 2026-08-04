#running sum of 1D Array
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runningSum=[]
        sums=0
        for i in nums:
            sums+=i
            runningSum.append(sums)
        return runningSum
        #time complexity = o(n)
        #space complexity = o(n)