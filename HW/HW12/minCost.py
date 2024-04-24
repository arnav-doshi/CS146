from typing import List

def minCostToSupplyWater(n: int, wells: List[int], pipes: List[List[int]]) -> int:
    visited = []
    total_cost = 0

    while len(visited) < n:
        best_pipe_cost = 99999999999999
        best_pipe_house = None

        for pipe in pipes:
            if pipe[0] in visited and pipe[1] not in visited:
                if pipe[2] < best_pipe_cost:
                    best_pipe_cost = pipe[2]
                    best_pipe_house = pipe[1]
            elif pipe[1] in visited and pipe[0] not in visited:
                if pipe[2] < best_pipe_cost:
                    best_pipe_cost = pipe[2]
                    best_pipe_house = pipe[0]

        best_well_cost = 99999999999999
        best_well_house = None
        for i, well_cost in enumerate(wells):
            if i + 1 not in visited and well_cost < best_well_cost:
                best_well_cost = well_cost
                best_well_house = i + 1

        if best_well_cost <= best_pipe_cost:
            total_cost += best_well_cost
            visited.append(best_well_house)
        else:
            total_cost += best_pipe_cost
            visited.append(best_pipe_house)

    return total_cost



## TEST
n = 2
wells = [1, 1]
pipes = [[1, 2, 1], [1, 2, 2]]
print(minCostToSupplyWater(n, wells, pipes))

