goal = [1,2,3,4,5,6,7,8,0]

def h(s):
    d = 0
    for i in range(9):
        if s[i] != 0:
            j = goal.index(s[i])
            d += abs(i//3 - j//3) + abs(i%3 - j%3)
    return d

def astar(start):
    open = [start]
    visited = []

    while open:
        s = min(open, key=h)
        open.remove(s)

        if s in visited:
            continue

        visited.append(s)

        print(s[:3])
        print(s[3:6])
        print(s[6:9])
        print()

        if s == goal:
            print("Goal Reached!")
            return

        z = s.index(0)

        for n in [z-3, z+3, z-1, z+1]:
            if 0 <= n < 9:
                if not (z%3 == 0 and n == z-1) and not (z%3 == 2 and n == z+1):
                    t = s.copy()
                    t[z], t[n] = t[n], t[z]

                    if t not in visited and t not in open:
                        open.append(t)

    print("No solution!")

start = list(map(int, input("Enter 9 numbers (0 for blank): ").split()))
astar(start)