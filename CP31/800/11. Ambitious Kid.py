n = int(input().strip())
a = list(map(int, input().split()))

diff = 100000

if 0 in a:
    print(0)
else:
    for i in a:
        ind_diff = abs(i)
        if ind_diff<diff:
            diff = ind_diff

    print(diff)