#capacity to ship packages within d days
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)

        while low <= high:
            mid = (low + high) // 2

            day = 1
            total = 0

            for weight in weights:
                if total + weight > mid:
                    day += 1
                    total = 0

                total += weight

            if day <= days:
                high = mid - 1
            else:
                low = mid + 1

        return low