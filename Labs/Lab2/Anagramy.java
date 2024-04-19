import java.util.*;

public class Anagramy {
    public static boolean anagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }

        HashMap<Character, Integer> count = new HashMap<>();

        for (char c : s.toCharArray()) {
            count.put(c, count.getOrDefault(c, 0) + 1);
        }

        for (char c : t.toCharArray()) {
            count.put(c, count.getOrDefault(c, 0) - 1);
        }

        for (HashMap.Entry<Character, Integer> entry : count.entrySet()) {
            if (entry.getValue() != 0) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        System.out.println(anagram("", "")); // T
        System.out.println(anagram("reed", "deer")); // T
        System.out.println(anagram("Anant", "Shukla")); // F
        System.out.println(anagram("aab", "bba")); // F
    }
}
