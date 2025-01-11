# Finding the number of stones in each pile

def test(n):
    return [n + 2 * i for i in range(n)]


n = 2

print("Number of piles:", n)
print("Number of stones in each pile:")
print(test(n))

n = 10

print("\nNumber of piles:", n)
print("Number of stones in each pile:")
print(test(n))

n = 3

print("\nNumber of piles:", n)
print("Number of stones in each pile:")
print(test(n))

n = 17

print("\nNumber of piles:", n)
print("Number of stones in each pile:")
print(test(n))
