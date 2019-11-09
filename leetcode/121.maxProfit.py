import sys


def maxProfit(prices):
    """
        :type prices: List[int]
        :rtype: int
        """
    # 暴力循环
    max_profit = 0
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            if prices[i] < prices[j]:
                max_profit = max(max_profit, prices[j] - prices[i])

    return max_profit


def maxProfit1(prices):
    if len(prices) < 2:
        return 0
    max_profit = 0
    min_price = prices[0]

    for p in prices:
        min_price = min(min_price, p)
        max_profit = max(max_profit, p - min_price)

    return max_profit


if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4, 1, 3]
    max_p = maxProfit1(prices)  #maxProfit(prices)
    print(max_p)
