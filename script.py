# script.py

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    c = 5
    for i in range(1, 1000000000):
        c += 1
    print(a + b)
