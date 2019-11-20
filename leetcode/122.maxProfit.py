def maxProfit(prices) -> int:
    profit: int = 0
    for i in range(1, len(prices)):
        temp = prices[i] - prices[i - 1]
        if temp > 0:
            profit += temp

    return profit


if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    profit = maxProfit(prices)
    print(profit)