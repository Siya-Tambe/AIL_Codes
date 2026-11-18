# Model based agent implementation for pathfinding in a grid environment
from collections import deque
grid = [
    [0, 0, 1, 0],
    [1, 0, 1, 0],
    [0, 0, 0, 0],
    [0, 1, 1, 0]
]
start = (0, 0)
goal = (3, 3)

q = deque([[start]])
memory = [start]

while q:
    path = q.popleft()
    r, c = path[-1]

    if (r, c) == goal:
        print("Path:", path)
        print("Goal Reached!")
        break

    for dr, dc in [(0,1), (1,0), (0,-1), (-1,0)]:
        nr, nc = r+dr, c+dc

        if (0 <= nr < 4 and 0 <= nc < 4 and
            grid[nr][nc] == 0 and (nr,nc) not in memory):

            memory.append((nr,nc))
            q.append(path + [(nr,nc)])
else:
    print("No Path Found!")
