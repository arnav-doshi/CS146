public class ChangeCoin {
    public int coinChange(int[] coins, int amount) {
        int[] memo = new int[amount + 1];
        for (int i = 0; i < memo.length; i++) {
            memo[i] = -1;
        }
        int answer = recurse(coins, amount, memo);

        if (answer != 99999999) {
            return answer;
        } else {
            return -1;
        }
    }

    public int recurse(int[] coins, int amount, int[] memo) {
        if (amount == 0) {
            return 0;
        }

        if (amount < 0) {
            return 99999999;
        }

        if (memo[amount] != -1) {
            return memo[amount];
        }

        int smallest = 99999999;

        for (int i = 0; i < coins.length; i++) {
            int next = amount - coins[i];
            int answer = recurse(coins, next, memo);

            if (answer != 99999999) {
                smallest = Math.min(smallest, answer + 1);
            }

        }

        memo[amount] = smallest;
        return memo[amount];
    }


    public static void main(String[] args) {
        ChangeCoin cc = new ChangeCoin();
        int[] coins = {1, 2, 5};
        int[] coins2 = {2};
        int[] coins3 = {1};

        System.out.println(cc.coinChange(coins, 11));
        System.out.println(cc.coinChange(coins2, 3));
        System.out.println(cc.coinChange(coins3, 0));
    }
    
   
}
