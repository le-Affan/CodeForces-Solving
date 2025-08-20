t = int(input().strip())

for i in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    if k == 1:
        if a == sorted(a):
            print("YES")
        else:
            print("NO")
    else:
        print("YES")