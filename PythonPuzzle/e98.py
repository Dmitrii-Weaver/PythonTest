# Compute the depth of groups of matched nested parentheses separated by parentheses
def test(parens):
    return [len(s.split(')')[0]) for s in parens.split()]


parentheses = '(()) (()) () ((()()())) '
print("Parentheses strings:", parentheses)
print("\nDepth of groups of matched nested parentheses separated by parentheses:")
print(test(parentheses))

parentheses = '() (()) () () () ()'
print("Parentheses strings:", parentheses)
print("\nDepth of groups of matched nested parentheses separated by parentheses:")
print(test(parentheses))

parentheses = '(((((((()))))))) () (()) ((()()()))'
print("Parentheses strings:", parentheses)
print("\nDepth of groups of matched nested parentheses separated by parentheses:")
print(test(parentheses))
