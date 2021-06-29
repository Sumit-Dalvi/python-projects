import random
password = ""
for x in range(8):
    cap = random.randint(64,90)
    small = random.randint(97,122)
    z = random.choice([cap , small])
    a = chr(z)
    password =  password + a
print(password)

