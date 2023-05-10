n = 1
s = 0
while n != 0:
    n = int(input())
    if n % 4 == 0 and n // 100 >= 1:
        s = s + 1
print(s)
