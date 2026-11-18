# DFS water jug problem
visited = set()
path = []

def dfs(a, b, target):

    if (a, b) in visited:
        return False

    visited.add((a, b))
    path.append((a, b))

    if a == target or b == target:
        print("Solution: ", path)
        return True

    moves = [
        (4, b), (a, 3),(0, b),(a, 0),
        (a - min(a, 3-b), b + min(a, 3-b)),
        (a + min(b, 4-a), b - min(b, 4-a)),
    ]

    for x, y in moves:
        if dfs(x, y, target):
            return True

    path.pop()
    return False

a = int(input("Enter initial water in Jug A: "))
b = int(input("Enter initial water in Jug B: "))
target = int(input("Enter target amount: "))

if not dfs(a, b, target):
    print("No solution!")
    