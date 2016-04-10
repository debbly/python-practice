def maxProfit(self, prices):
    if not prices: return 0
    MIN = prices[0]
    res = 0
    prices.pop(0)
    for p in prices:
        if p < MIN:
            MIN = p
        elif p > MIN:
            red = max(res, p - MIN)
    return res
