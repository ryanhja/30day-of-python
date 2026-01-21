# Day 10: 30 Days of python programming

print("Loop for")
for i in range (10):
    print(i)

print("Loop white")
count = 0
while count < 10:
    print(count)
    count += 1

print("Triangle")
motif = "#"
for i in range(1, 8):
    print(motif * i)


print("\nSquare")
s_width = 8
motif = "*"
for i in range(1,s_width + 1):
    print(f"{motif} " * s_width)

print("\nMultiplication")
for i in range(11):
    print(f"{i} x {i} = {i*i}")