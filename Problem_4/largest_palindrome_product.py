def is_palindrome(num):
    return str(num) == str(num)[::-1]

max = 0

for x in reversed(range(100, 1000)):
    for y in reversed(range(100, 1000)):
        suspect = x*y
        if is_palindrome(suspect):
            if suspect > max:
                max = suspect

print(max)
        
