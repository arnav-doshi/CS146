import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class MeetingRooms {
    
    public int minMeetingRooms(int[][] intervals) {      
        if (intervals.length == 0) {
            return 0;
        }
    
        HashMap<Integer, Integer> hashy = new HashMap<>();
        
        for (int[] i : intervals) {
            for (int j = i[0]; j < i[1]; j++) {
                Integer value = hashy.get(j);
                if (value == null)
                hashy.put(j, 1);
                else
                hashy.put(j, value + 1);
            }
        }

        int num = Integer.MIN_VALUE;
        for (Map.Entry<Integer, Integer> entry : hashy.entrySet()) {
            Integer value = entry.getValue();

            if (value > num)
            num = value;
    
        }

        return num;



    }

    public static void main(String[] args) {
        int[][] intervals = {{0,1} , {1,2}, {2,3}};
        MeetingRooms mr = new MeetingRooms();
        System.out.println(mr.minMeetingRooms(intervals));


        int[][] intervals2 = {{0,10} , {5,15}, {10,20}};
        System.out.println(mr.minMeetingRooms(intervals2));
    }


}
