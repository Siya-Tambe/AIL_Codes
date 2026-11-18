
# Goal Stack Planning for Blocks World

blocks = ["A", "B", "C"]
pos = {"A": "table", "B": "table", "C": "table"}

def clear(x):
    for b in blocks:
        if pos[b] == x:
            clear(b)
            pos[b] = "table"
            print("Move", b, "to table")

goal_stack = [("C", "B"), ("B", "A")]

while goal_stack:
    x, y = goal_stack.pop()

    if pos[x] != y:
        clear(x)
        clear(y)
        pos[x] = y
        print("Move", x, "on", y)

print("Goal Achieved!")
print(pos)



