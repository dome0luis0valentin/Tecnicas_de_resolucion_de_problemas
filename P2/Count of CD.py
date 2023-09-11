import sys

line = sys.stdin.readline()
Jacks_cd = set({})

cant_rep = 0

N = int(line.split()[0])
M = int(line.split()[1])

while (N != 0 or M != 0)and(line):
    cant_rep = 0
    for I in range(N):
        CD = sys.stdin.readline()
        Jacks_cd.add(CD)

    for J in range(M):
        CD = sys.stdin.readline()
        if CD in Jacks_cd:
            cant_rep += 1

    if not(N == 0 or M == 0):
        sys.stdout.write(str(cant_rep)+"\n")
    
    line = sys.stdin.readline()
    N = int(line.split()[0])
    M = int(line.split()[1])


