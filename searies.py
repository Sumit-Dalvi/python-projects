
number = [0, 1]
for x in range(2, 50):
    m = number[x-1] + number[x-2]
    number.append(m)
print(number)
