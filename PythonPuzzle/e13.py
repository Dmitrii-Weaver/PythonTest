# Find the strings in a list, starting with a given prefix

def test(strs, prefix):
    return [s for s in strs if s.startswith(prefix)]


strs = ['cat', 'car', 'fear', 'center']
prefix = "ca"

print("Original strings:")
print(strs)

print("Starting prefix:", prefix)

print("Strings in the said list starting with a given prefix:")

print(test(strs, prefix))

strs = ['cat', 'dog', 'shatter', 'donut', 'at', 'todo']
prefix = "do"

print("\nOriginal strings:")
print(strs)

print("Starting prefix:", prefix)
print("Strings in the said list starting with a given prefix:")
print(test(strs, prefix))
