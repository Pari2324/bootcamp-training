#Find numbers with even digit of numbers
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for i in nums:
            a = str(i)
            if len(a)%2==0:
                count+=1
        return count

        #Time Complexity = O(n × d).
        #Space Complexity = O(d)