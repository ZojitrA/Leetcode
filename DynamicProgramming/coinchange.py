class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dynamic_table = [0]+[float('inf') for el in range(amount)]
        for i in range(1, len(dynamic_table)):
            for coin in coins:
                if i - coin >= 0:
                    dynamic_table[i] = min(dynamic_table[i - coin] + 1, dynamic_table[i])

        return dynamic_table[-1] if dynamic_table[-1] < float('inf') else -1
            
