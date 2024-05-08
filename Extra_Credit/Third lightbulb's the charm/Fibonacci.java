public class Fibonacci {

    public static int fib(int n) {
        if (n == 1 || n == 2) {
            return 1;
        }

        int[] bottomUp =  new int[n+1];

        for (int i = 0; i < bottomUp.length; i++) {
            bottomUp[i] = -1;
        }

        bottomUp[1] = 1;
        bottomUp[2] = 1;

        for (int j = 3; j <= n; j++) {
            bottomUp[j] = bottomUp[j-2] + bottomUp[j-1];
        }

        return bottomUp[n];
    }
    

    public static void main(String[] args) {
        System.out.println(fib(20));
    }
    
}
