class Solution:
    # Time Complexity : O (n^2)
    # Space Complexit: O(1)
    # Brute Force Solution
    # For every stock at ith position, Find the max of all the selling options in the future.
    # Time Limit Exceeded on Leetcode
    def maxProfit_bruteForce(self, prices: List[int]) -> int:
        if not prices:
            return 0
        max_profit = 0
        for i in range(len(prices)):
            max_profit = max(max_profit,max(prices[i:]) - prices[i])
        return max_profit
    
    # Optimitized Solution
    #
    def maxProfit_optimized(self,prices):
        # Solution accepted on leetcode
        # Update the minimum to find the best stock to buy and find the profit with very iteration with the best buying stock
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        if not prices:
            return 0
        min_price = prices[0]
        max_profit = 0
        for i in range(1,len(prices)):
            max_profit = max(max_profit,prices[i]- min_price)
            if prices[i] < min_price:
                min_price = prices[i]
        return max_profit