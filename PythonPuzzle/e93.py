# Closest Palindrome to String

def test(s):
    odd = 0

    for i, c in enumerate(s):
        if c != s[~i]:
            odd += 1

    if odd % 2 == 1:
        half = odd // 2
        pal = "".join((s[i] if i < half else s[~i] for i in range(len(s))))
        return pal
    else:
        half = odd // 2
        pal = "".join((s[i] if i <= half else s[~i] for i in range(len(s))))
        return pal


s1 = "cat"
print("Original string:", s1)
print("Closest palindrome of the said string:")
print(test(s1))

s2 = "madan"
print("\nOriginal string:", s2)
print("Closest palindrome of the said string:")
print(test(s2))

s3 = "radivider"
print("Original string:", s3)
print("Closest palindrome of the said string:")
print(test(s3))

s4 = "madan"
print("\nOriginal string:", s4)
print("Closest palindrome of the said string:")
print(test(s4))

s5 = "abc"
print("Original string:", s5)
print("Closest palindrome of the said string:")
print(test(s5))

s6 = "racecbr"
print("\nOriginal string:", s6)
print("Closest palindrome of the said string:")
print(test(s6))
