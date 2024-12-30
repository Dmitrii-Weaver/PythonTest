# Replace Spaces with Underscore and Hyphen
def test(strs):
    return strs.replace("-", " " * 3).replace("_", " ")


strs = "Python-Exercises"
print("Original strings:", strs)
print("Depth of groups of matched nested parentheses separated by parentheses:")
print(test(strs))

strs = "Python_Exercises"
print("\nOriginal strings:", strs)
print("Depth of groups of matched nested parentheses separated by parentheses:")
print(test(strs))

strs = "-Hello,_world!__This_is-so-easy!-"
print("\nOriginal strings:", strs)
print("Depth of groups of matched nested parentheses separated by parentheses:")
print(test(strs))
