#!/bin/python3
#This was elegant solution I would like to study later
import math
import os
import random
import re
import sys
from collections import deque
# Complete the roadsAndLibraries function below.
def generate_graph(connections):
    graph = {}
    for con in connections:
        graph[con[0]] = [con[1]] if con[0] not in graph else graph[con[0]] + [con[1],]
        graph[con[1]] = [con[0]] if con[1] not in graph else graph[con[1]] + [con[0],]
    return graph
def roadsAndLibraries(n, c_lib, c_road, cities):
    graph = generate_graph(cities)
    visited = set()
    q = deque()
    road_count = 0
    library_count = 0
    if c_lib < c_road:
        return n*c_lib
    for city in range(1, n+1):
        if city not in visited:
            library_count += 1
            q.append(city)
            visited.add(city)
            while q:
                n = q.pop()
                if n in graph:
                    for nbour in graph[n]:
                        if nbour not in visited:
                            road_count += 1
                            q.append(nbour)
                            visited.add(nbour)
    return library_count*c_lib + road_count*c_road
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        nmC_libC_road = input().split()

        n = int(nmC_libC_road[0])

        m = int(nmC_libC_road[1])

        c_lib = int(nmC_libC_road[2])

        c_road = int(nmC_libC_road[3])

        cities = []

        for _ in range(m):
            cities.append(list(map(int, input().rstrip().split())))

        result = roadsAndLibraries(n, c_lib, c_road, cities)

        fptr.write(str(result) + '\n')

    fptr.close()

