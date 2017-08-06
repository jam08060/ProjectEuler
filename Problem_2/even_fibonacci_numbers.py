def fibonacci():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a+b

sum = 0
for f in fibonacci():
    if f > 4000000:
        break
    if f % 2 == 0:
        sum += f

print(sum)

