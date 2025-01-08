# List of integers where the sum of the first i integers is i

def test(li, i):
    return sum(li[:i]) == i


nums = [0, 1, 2, 3, 4, 5]

i = 1

print("Original list:")
print(nums)

print("Check the said list, where the sum of the first i integers is i: i =", i)

print(test(nums, 1))

i = 3

print("\nOriginal list:")
print(nums)

print("Check the said list, where the sum of the first i integers is i: i =", i)
print(test(nums, 3))

i = 6
nums = [1, 1, 1, 1, 1, 1]

print("\nOriginal list:")
print(nums)

print("Check the said list, where the sum of the first i integers is i: i =", i)
print(test(nums, 6))

i = 2
nums = [2, 2, 2, 2, 2]

print("\nOriginal list:")
print(nums)

print("Check the said list, where the sum of the first i integers is i: i =", i)
print(test(nums, 2))
