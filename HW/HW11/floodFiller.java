public class floodFiller {
    public int[][] floodFill(int[][] image, int sr, int sc, int newColor) {
        if (image == null || image.length == 0 || image[0].length == 0) {
            return new int[0][0];
        }
        
        int color1 = image[sr][sc];
        int width = image.length;
        int height = image[0].length;

        flood(image, sr, sc, newColor, color1, width, height);
        return image;
    }
    
    public void flood(int[][] image, int sr, int sc, int color2, int color1, int width, int height) {
        if (sr < 0 || sr >= width) {
            return;
        }

        if (sc < 0 || sc >= height) {
            return;
        }

        if (image[sr][sc] == color2) {
            return;
        }

        if (image[sr][sc] != color1) {
            return;
        }

        image[sr][sc] = color2;

        flood(image, sr + 1, sc, color2, color1, width, height);
        flood(image, sr, sc + 1, color2, color1, width, height);

        flood(image, sr - 1, sc, color2, color1, width, height);
        flood(image, sr, sc - 1, color2, color1, width, height);
    }

    public static void main(String[] args) {
        // int[][] image = {
        //     {1, 1, 1},
        //     {1, 1, 0},
        //     {1, 0, 1}
        // };
        // int sr = 1;
        // int sc = 1;
        // int color = 2;

        // floodFiller ff = new floodFiller();
        // int[][] tester = ff.floodFill(image, sr, sc, color);

        // System.out.println(java.util.Arrays.deepToString(tester));

    }
    
        
}
    
        
    