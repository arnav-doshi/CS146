public class BadVersion {
    public static int firstBadVersion(int number) {
        int left = 1;
        int right = number;

        while (right > left) {
            int midd = left + (right - left) / 2;
            if (isBadVersion(midd)) {
                right = midd; 
            } else {
                left = midd+1;
            }

        }
        return left;
    }
    
}
