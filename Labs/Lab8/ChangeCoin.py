class changeCoin:
    def coinChange(self, coins, amount):
        memo = [-1] * (amount + 1)
        answer = self.recurse(coins, amount, memo)

        if (answer != 99999999):
            return answer
        else:
            return -1

    def recurse(self, coins, amount, memo):
        if (amount == 0):
            return 0
        
        if (amount < 0):
            return 99999999
        
        if (memo[amount] != -1):
            return memo[amount]
        
        smallest = 99999999
        coinSize = len(coins)

        for i in range (0, coinSize):
            next = amount - coins[i]
            answer = self.recurse(coins, next, memo)
            if(answer != 99999999):
                smallest = min(smallest, answer+1)
        
        memo[amount] = smallest
        return memo[amount]




cc = changeCoin()
print(cc.coinChange([1,2,5], 11))
# print(cc.coinChange([2], 3))
# print(cc.coinChange([1], 0))