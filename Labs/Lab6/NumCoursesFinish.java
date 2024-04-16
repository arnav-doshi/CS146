import java.util.*;

public class NumCoursesFinish {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        Map<Integer, Integer> inDegree = new HashMap<>();
        Queue<Integer> queue = new LinkedList<>();

        for (int c = 0; c < numCourses; c++) {
            inDegree.put(c, 0);
        }

        for (int[] p : prerequisites) {
            int course = p[0];
            inDegree.put(course, inDegree.getOrDefault(course, 0) + 1);
        }

        for (int course = 0; course < numCourses; course++) {
            if (inDegree.get(course) == 0) {
                queue.add(course);
            }
        }

        int coursesDone = 0;

        while (!queue.isEmpty()) {
            int course = queue.poll();
            coursesDone++;

            for (int[] p2 : prerequisites) {
                int c = p2[0];
                int prereq = p2[1];
                if (prereq == course) {
                    inDegree.put(c, inDegree.get(c) - 1);
                    if (inDegree.get(c) == 0) {
                        queue.add(c);
                    }
                }
            }
        }

        return coursesDone == numCourses;
    }

    public static void main(String[] args) {
        NumCoursesFinish numcoursesfinish = new NumCoursesFinish();
        int[][] prerequisites = {{1,0}, {2,1}, {3,2}, {4,3}, {0,4}};
        int numCourses = 5;
        System.out.println(numcoursesfinish.canFinish(numCourses, prerequisites));
    }

}

