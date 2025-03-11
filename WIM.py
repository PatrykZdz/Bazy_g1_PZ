
an = [[1, 1, 1, 1, 3, 1],
    [1, 1, 1, 1, 3, 2],
    [1, 1, 1, 3, 2, 1],
    [1, 1, 1, 3, 3, 2],
    [1, 1, 2 ,1, 2, 1],
    [1, 1, 2, 1, 2, 2],
    [1, 1, 2, 2, 3, 1],
    [1, 1, 2, 2, 4, 1]]

d = [[1], [1], [0], [1], [0], [1], [0], [1]]

for x in range(len(an)):
    print(f"{an[x]}{d[x]}")

#i = 1
#for x in range(len(an)-1):
#    for y in range(len(an)-1):
#        if an[x][y] != an[x+i][y]:
#            print([y])


for x in range(len(an)):
    for y in range(len(an)-2):
        print(f"{x,y} = {an[x][y]}")








