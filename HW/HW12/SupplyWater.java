import java.util.*;

public class SupplyWater {

    public int minCostToSupplyWater(int n, int[] wells, int[][] pipes) {
        List<Integer> visited = new ArrayList<>();
        int totalCost = 0;

        while (visited.size() < n) {
            int bestPipeCost = Integer.MAX_VALUE;
            int bestPipeHouse = -1;

            for (int[] pipe : pipes) {
                if (visited.contains(pipe[0]) && !visited.contains(pipe[1])) {
                    if (pipe[2] < bestPipeCost) {
                        bestPipeCost = pipe[2];
                        bestPipeHouse = pipe[1];
                    }
                } else if (visited.contains(pipe[1]) && !visited.contains(pipe[0])) {
                    if (pipe[2] < bestPipeCost) {
                        bestPipeCost = pipe[2];
                        bestPipeHouse = pipe[0];
                    }
                }
            }

            int bestWellCost = Integer.MAX_VALUE;
            int bestWellHouse = -1;
            for (int i = 0; i < wells.length; i++) {
                if (!visited.contains(i + 1) && wells[i] < bestWellCost) {
                    bestWellCost = wells[i];
                    bestWellHouse = i + 1;
                }
            }

            if (bestWellCost <= bestPipeCost) {
                totalCost += bestWellCost;
                visited.add(bestWellHouse);
            } else {
                totalCost += bestPipeCost;
                visited.add(bestPipeHouse);
            }
        }

        return totalCost;
    }

// TEST BELOW
    public static void main(String[] args) {
        SupplyWater water = new SupplyWater();
        int n = 2;
        int[] wells = {1,1};
        int[][] pipes = {{1, 2, 1}, {1, 2, 2}};
        System.out.println(water.minCostToSupplyWater(n, wells, pipes));
    }
}
