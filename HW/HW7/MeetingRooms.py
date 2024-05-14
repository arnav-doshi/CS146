from typing import List

class MeetingRooms:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:   
        if not intervals:
            return 0
        
        hashy = {}
        
        for i in intervals:
            for j in range(i[0], i[1]):
                if j not in hashy:
                    hashy[j] = 1
                else:
                    hashy[j] += 1
        
        num = -99999999999999999
        for value in hashy.values():
            if value > num:
                num = value
        
        return num


mr = MeetingRooms()
intervals = [[0,1], [1,2], [2,3]]
print(mr.minMeetingRooms(intervals))

intervals2 = [[0,10], [5,15], [10,20]]
print(mr.minMeetingRooms(intervals2))

