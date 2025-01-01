#Find the lengths of a list of non-empty strings

def test(strs):
    return [*map(len, strs)]
strs = ['cat', 'car', 'fear', 'center']

print("Original strings:")
print(strs)

print("Lengths of the said list of non-empty strings:")
print(test(strs))

strs = ['cat', 'dog', 'shatter', 'donut', 'at', 'todo', '']

print("\nOriginal strings:")
print(strs)

print("Lengths of the said list of non-empty strings:")
print(test(strs))