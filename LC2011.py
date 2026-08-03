#final value of variable after performing operations
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        for i in operations:
            if i == "++X" or i == "X++":
             x = x + 1
            else:
             x = x - 1
        return x
        #time complexity = o(n)
        #space complexity = o(1)
            