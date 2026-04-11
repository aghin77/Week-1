# Day 5 - Control Flow (while, for)

# 1. Basic For Loop
print("1. Numbers from 1 to 10:")
for i in range(1, 11):
    print(i)

print("\n----------------------\n")

# 2. String Iteration
name = "Aghin"  # change this to your name
print("2. Characters in the name:")
for char in name:
    print(char)

print("\n----------------------\n")

# 3. While Loop - Countdown Timer
print("3. Countdown Timer:")
count = 10
while count >= 0:
    print(count)
    count -= 1

print("\n----------------------\n")

# 4. Sum of Numbers (1 to 50)
print("4. Sum of numbers from 1 to 50:")
total = 0
for i in range(1, 51):
    total += i
print("Sum =", total)

print("\n----------------------\n")

# 5. Break and Continue

print("5a. Break when number is 7:")
for i in range(1, 11):
    if i == 7:
        break
    print(i)

print("\n5b. Skip number 5 using continue:")
for i in range(1, 11):
    if i == 5:
        continue
    print(i)

print("\n----------------------\n")

# 6. Nested Loops - 5x5 Square of Stars
print("6. 5x5 Square of Stars:")
for i in range(5):
    for j in range(5):
        print("*", end=" ")
    print()  # new line after each row