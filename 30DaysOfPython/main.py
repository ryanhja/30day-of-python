arr = [
    [1, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0],
    [0, 0, 2, 4, 4, 0],
    [0, 0, 0, 2, 0, 0],
    [0, 0, 1, 2, 4, 0]
]

hourglass = []
for a in arr:
    sum_a = 0
    for i in range(3):
        sum_a += a[i]
    hourglass.append(sum_a)

print(hourglass)
