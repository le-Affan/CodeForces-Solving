from collections import defaultdict

t = int(input().strip())

for i in range(t):
    n = int(input().strip())
    a = list(map(int, input().split()))

    if n == 2:
        print("Yes")
    elif n > 2:
        if len(set(a)) == 1:
            print("Yes")
        elif len(set(a)) == 2:
            freq = defaultdict(int)

            for i in a:
                freq[i] += 1

            counts = list(freq.values())

            if abs(counts[0] - counts[1]) <= 1:
                print("Yes")
            else:
                print("No")

        else:
            print("No")