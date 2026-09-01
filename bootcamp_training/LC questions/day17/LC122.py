#best time to buy and sekk stock 11
profit = 0

        # Every upward step can be taken as a separate transaction.
        # Adding all positive day-to-day gains equals the optimal total profit.
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]

        return profit