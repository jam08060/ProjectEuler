from math import sqrt, ceil

subject = 600851475143
suspect = subject
result = 0

counter = 2
while counter <= sqrt(suspect):
    if suspect % counter == 0:
        suspect /= counter
        result = counter
    else:
        counter+=1
if suspect > result:
    result = suspect

print(int(result))
