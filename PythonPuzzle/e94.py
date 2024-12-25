# Split Matched Parentheses Groups

def test(combined):
    ls = []
    s2 = ""

    for s in combined.replace(' ', ''):
        s2 += s

        if s2.count("(") == s2.count(")"):
            ls.append(s2)

            s2 = ""

    return ls


combined1 = '( ()) ((()()())) (()) ()'
print("Parentheses string:")
print(combined1)
print("Separate parentheses groups of the said string:")
print(test(combined1))

combined2 = '() (( ( )() (   )) ) ( ())'
print("\nParentheses string:")
print(combined2)
print("Separate parentheses groups of the said string:")
print(test(combined2))
