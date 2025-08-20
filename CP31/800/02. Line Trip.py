t = int(input().strip())

for i in range(t):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))

    initial_dist = (abs(0 - a[0]))
    final_dist = 2 * (abs(a[len(a) - 1] - x))

    max_dist = max(initial_dist, final_dist)

    for i in range(len(a) - 1):
        ind_dist = abs(a[i] - a[i + 1])
        if ind_dist > max_dist:
            max_dist = ind_dist

    print(max_dist)