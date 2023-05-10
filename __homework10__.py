n = 1
s = 0
while n % 10 != 0:
    n = int(input())
    if n % 5 == 0:
        s = s + 1

print(s)
