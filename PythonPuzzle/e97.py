# Strange sort of list of numbers

def test(nums):
    if len(nums) < 2:
        return nums
    result = []

    for i in range(len(nums)//2):
        result.append(min(nums))
        nums.remove(min(nums))
        result.append(max(nums))
        nums.remove(max(nums))

    if len(nums) > 0:
        result.append(nums[0])
    if len(result) < 2 * len(nums):
        result.extend(nums[len(result) // 2 + 1:len(result) //
                      2 + 1 + len(nums) - len(result)])
    return result


nums = [1, 3, 4, 5, 11]
print("Original list of numbers:")
print(nums)
print("Strange sort of list of said numbers:")
print(test(nums))

nums = [27, 3, 8, 5, 1, 31]
print("\nOriginal list of numbers:")
print(nums)
print("Strange sort of list of said numbers:")
print(test(nums))

nums = [1, 2, 7, 3, 4, 5, 6]
print("\nOriginal list of numbers:")
print(nums)
print("Strange sort of list of said numbers:")
print(test(nums))
