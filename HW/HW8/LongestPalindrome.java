import java.util.*;


public class LongestPalindrome {
    public int longestPalindrome(String s) {
        
        if (s.isEmpty()) 
            return 0;

        if (s.length() == 1) 
            return 1;

        boolean odd = false;
        HashMap<Character, Integer> hashy = new HashMap<>();
        int output = 0;

        for (char c : s.toCharArray()) {
            if (!hashy.containsKey(c)) 
                hashy.put(c, 1);
             else 
                hashy.put(c, hashy.get(c) + 1);
            
        }

        for (char c : hashy.keySet()) {
            if (hashy.get(c) % 2 == 0) {
                output += hashy.get(c);
            } else {
                output += (hashy.get(c) - 1);
                odd = true;
            }
        }

        if (odd) {
            output++;
            return output;
        }

        return output;
    }

    public static void main(String[] args) {
        LongestPalindrome lp = new LongestPalindrome();
        System.out.println(lp.longestPalindrome("abccccdd"));
    }
}
