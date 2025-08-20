t = int(input().strip())

for i in range(t):
    n = int(input().strip())
    a = list(map(int, input().split()))

    if a == sorted(a):
        print("Yes")

    else:
        sorted_a = a[:]
        change = True

        while change:
            change = False
            for i in range(1, n - 1):
                if sorted_a[i] > sorted_a[i + 1] and sorted_a[i] > sorted_a[i - 1]:
                    sorted_a[i], sorted_a[i + 1] = sorted_a[i + 1], sorted_a[i]
                    change = True

        if sorted_a == sorted(a):
            print("Yes")
        else:
            print("No")