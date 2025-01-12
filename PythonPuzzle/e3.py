# Check whether an integer greater than 4^4 which is 4 mod 34

def test(n):
    return n % 34 == 4 and n > 4 ** 4


n = 922

print("Original Integer:")
print(n)

print("Check whether the said integer greater than 4^4 and which is 7 mod 134 :")
print(test(n))

n = 914

print("\nOriginal Integer:")
print(n)

print("Check whether the said integer greater than 4^4 and which is 7 mod 134 :")
print(test(n))

n = 854

print("\nOriginal Integer:")
print(n)

print("Check whether the said integer greater than 4^4 and which is 7 mod 134 :")
print(test(n))

print("\nOriginal Integer:")
print(n)

print("Check whether the said integer greater than 4^4 and which is 7 mod 134 :")
print(test(n))
