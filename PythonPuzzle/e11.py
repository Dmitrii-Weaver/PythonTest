# Find the indexes of numbers, below a given threshold

def test(nums, thresh):
    return [i for i, n in enumerate(nums) if n < thresh]


nums = [0, 12, 45, 3, 4923, 322, 105, 29, 15, 39, 55]
thresh = 100

print("Original list:")
print(nums)

print("Threshold: ", thresh)
print("Check the indexes of numbers of the said list below the given threshold:")
print(test(nums, thresh))

nums = [0, 12, 4, 3, 49, 9, 1, 5, 3]
thresh = 10

print("\nOriginal list:")
print(nums)

print("Threshold: ", thresh)
print("Check the indexes of numbers of the said list below the given threshold:")

print(test(nums, thresh))
