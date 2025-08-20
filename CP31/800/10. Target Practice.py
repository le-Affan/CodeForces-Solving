t = int(input().strip())

for i in range(t):
    points = 0
    for j in range(10):
        line = input().strip()

        if j in [0,9]:
            for k in range(10):
                if line[k]=='X':
                    points += 1

        elif j in [1,8]:
            for k in range(10):
                if line[k]=='X' and (k in [0,9]):
                    points += 1
                elif line[k]=='X':
                    points += 2

        elif j in [2,7]:
            for k in range(10):
                if line[k]=='X' and (k in [1,8]):
                    points += 2
                elif line[k]=='X' and (k in [0,9]):
                    points += 1
                elif line[k]=='X':
                    points += 3

        elif j in [3,6]:
            for k in range(10):
                if line[k]=='X' and (k in [1,8]):
                    points += 2
                elif line[k]=='X' and (k in [0,9]):
                    points += 1
                elif line[k]=='X' and (k in [2,7]):
                    points += 3
                elif line[k]=="X":
                    points += 4

        elif j in [4,5]:
            for k in range(10):
                if line[k]=='X' and (k in [1,8]):
                    points += 2
                elif line[k]=='X' and (k in [0,9]):
                    points += 1
                elif line[k]=='X' and (k in [2,7]):
                    points += 3
                elif line[k]=="X" and (k in [3,6]):
                    points += 4
                elif line[k]=="X":
                    points += 5

    print(points)
