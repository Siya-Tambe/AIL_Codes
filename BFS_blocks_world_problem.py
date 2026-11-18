# BFS for block world problem
from collections import deque

def bfs(start, goal):
    q = deque([(start, [start])])
    visited = [start]

    while q:
        state, path = q.popleft()

        if state == goal:
            print("Solution: ",path)
            return 

        for i in range(3):
            for j in range(3):
                if i != j and state[i] != "":
                    new = list(state)
                    block = new[i][-1]
                    new[i] = new[i][:-1]
                    new[j] += block

                    new = tuple(new)

                    if new not in visited:
                        visited.append(new)
                        q.append((new, path + [new]))

    print("No solution!")

start = ("ABC","","")
goal = ("CBA","","")

bfs(start, goal) 