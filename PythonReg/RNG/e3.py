import secrets

secretsGenerator = secrets.SystemRandom()

print("Generating 6 digit random OTP")
otp = secretsGenerator.randrange(100000, 999999)

print("The random OTP is ", otp)