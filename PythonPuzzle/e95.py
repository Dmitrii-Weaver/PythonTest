# Find a palindrome of a given length containing a given string


def test(s, length):
    s_index = 0
    length_half = (length - (length % 2)) // 2
    ans = ""
    while len(ans) < length_half:
        ans += s[s_index % len(s)]
        s_index += 1

    if length % 2 == 1:
        ans += "a"

    return ans + ans[::-1]


s = 'madam'
length = 7
print("String and length of the palindrome:", s, ",", length)
print("Palindrome of the said string and length:")
print(test(s, length))

s = 'madam'
length = 6
print("\nString and length of the palindrome:", s, ",", length)
print("Palindrome of the said string and length:")
print(test(s, length))

length = 5
print("\nString and length of the palindrome:", s, ",", length)
print("Palindrome of the said string and length:")
print(test(s, length))

length = 3
print("\nString and length of the palindrome:", s, ",", length)
print("Palindrome of the said string and length:")
print(test(s, length))

length = 2
print("\nString and length of the palindrome:", s, ",", length)
print("Palindrome of the said string and length:")
print(test(s, length))

length = 1
print("\nString and length of the palindrome:", s, ",", length)
print("Palindrome of the said string and length:")
print(test(s, length))
