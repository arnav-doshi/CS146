def canFinish(numCourses, prerequisites):
    inDegree = {}
    queue = []

    for c in range(numCourses):
        inDegree[c] = (0)

    for course, a in prerequisites:
        if course in inDegree:
            inDegree[course] += 1
        else:
            inDegree[course] = 1

    for course in range(numCourses):
        if inDegree[course] == 0:
            queue.append(course)

    coursesDone = 0
    
    while queue:
        course = queue.pop(0)  
        coursesDone += 1 

        for c, prereq in prerequisites:
            if prereq == course:
                inDegree[c] -= 1
                if inDegree[c] == 0:
                    queue.append(c)

    return coursesDone == numCourses

# numCourses = 5
# prerequisites = [[1, 0], [2, 1], [3, 2], [4, 3], [0, 4]]

numCourses = 2
prerequisites = [[1, 0], [0, 1]]
print(canFinish(numCourses, prerequisites)) 
