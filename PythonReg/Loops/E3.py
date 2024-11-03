s = 0
n = int(input("Enter number "))
for i in range(1, n + 1, 1):
    s += i
print("\n")
print("Sum is: ", s)


# alt 

n = int(input("Enter number "))
x = sum(range(1, n + 1))
print('Sum is:', x)