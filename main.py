import random
import numpy as np
import time
from BFS import BFS
from AStar import AStarSearch
import statistics
from graphicsUtil import draw, print_table

#inp = [[1, 8, 2], [-1, 4, 3], [7, 6, 5]]
#out = [[1, 2, 3], [ 4, 5, 6], [ 7, 8, -1]]

#inp = [[1, 2, 3], [4, -1, 5], [6, 7, 8]]
#out = [[1, 2, 3], [6, 4, 5], [-1, 7, 8]]


inp = [ [[1, 8, 2], [-1, 4, 3], [7, 6, 5]],
    [[1,2,3], [8, -1, 4], [7, 6, 5]],
[[1, 2, 3], [4, -1, 5], [6, 7, 8]] ]

out = [
[[1, 2, 3], [ 4, 5, 6], [ 7, 8, -1]],
    [[2, 8, 1], [-1, 4, 3], [7, 6, 5]],
[[1, 2, 3], [6, 4, 5], [-1, 7, 8]]
]


def dfs(inp, out):
    print('Start dfs')
    search = BFS()

    start = time.time()
    delta_memory = search.find_solution(inp, out)

    end = time.time()

    print("Input: ", inp)
    # print("result: ", "no res" if res is None else res.state)
    deltaSec = end - start
    return deltaSec, delta_memory

def aStar(inp, out):
    print('Start aStar')
    search = AStarSearch()

    start = time.time()
    delta_memory = search.find_solution(inp, out)
    end = time.time()

    print("Input: ", inp)
    # print("result: ", res.state)
    deltaSec = end - start
    return deltaSec, delta_memory

sessionsCount = 3
average_aStar_session_memory_usage = []
average_dfs_session_memory_usage = []

average_aStar_session_time = []
average_dfs_session_time = []


for sessionIndex in range(sessionsCount):
    experimentcount = 1

    session_aStar_time = []
    session_ldfd_time = []
    session_aStar_memory_usage = []
    session_dfs_memory_usage = []

    dfs_time, dfs_space = dfs(inp[sessionIndex], out[sessionIndex])
    a_star_time, a_star_space = aStar(inp[sessionIndex], out[sessionIndex])

    session_ldfd_time.append(round(dfs_time, 7))
    session_aStar_time.append(round(a_star_time, 7))

    session_dfs_memory_usage.append(round(dfs_space, 7))
    session_aStar_memory_usage.append(round(a_star_space, 7))
    print("------------------------------------------\n")

    average_dfs_session_time.append(statistics.mean(session_ldfd_time))
    average_aStar_session_time.append(statistics.mean(session_aStar_time))

    average_dfs_session_memory_usage.append(statistics.mean(session_dfs_memory_usage))
    average_aStar_session_memory_usage.append(statistics.mean(session_aStar_memory_usage))

    print("Time ")
    print_table(experimentcount, session_aStar_time, session_ldfd_time, average_aStar_session_time[sessionIndex], average_dfs_session_time[sessionIndex])

    print("States")
    print_table(experimentcount, session_aStar_memory_usage, session_dfs_memory_usage, average_aStar_session_memory_usage[sessionIndex], average_dfs_session_memory_usage[sessionIndex])

    draw(f"Test case{sessionIndex+1}: Time", experimentcount, session_aStar_time, session_ldfd_time)
    draw(f"Test Case{sessionIndex+1}: States", experimentcount, session_aStar_memory_usage, session_dfs_memory_usage)


print("Average time per algorithm")
a_average_dfs_time = statistics.mean(average_dfs_session_time)
a_average_aStar_time = statistics.mean(average_aStar_session_time)
print_table(sessionsCount, average_aStar_session_time, average_dfs_session_time, a_average_aStar_time, a_average_dfs_time)

print("Average states per algorithm")
a_average_dfs_memory = statistics.mean(average_dfs_session_memory_usage)
a_average_aStar_memory = statistics.mean(average_aStar_session_memory_usage)
print_table(sessionsCount, average_aStar_session_memory_usage, average_dfs_session_memory_usage, a_average_aStar_memory, a_average_dfs_memory)

draw("Average time", sessionsCount, average_aStar_session_time, average_dfs_session_time)
draw("Average states", sessionsCount, average_aStar_session_memory_usage, average_dfs_session_memory_usage)
