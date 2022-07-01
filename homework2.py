import itertools

base= (0,2)
points=( (2,5), (5,2), (6,6), (8,3) )
minpath = 10**len(points)
for i in itertools.permutations(points, 4):
    way=0
    path=[]
    start = base
    for point in i:
        path_lnght = ((point[0] - start[0]) ** 2 + (point[1] - start[1]) ** 2) ** 0.5
        path.append((point, path_lnght))
        way += path_lnght
        start = point
    point = base
    path_lnght = ((point[0] - start[0]) ** 2 + (point[1] - start[1]) ** 2) ** 0.5
    path.append((point, path_lnght))
    way += path_lnght
    if way<minpath:
        bestpath=path
        minpath = way
print(base, end="")
for i in bestpath:
    print("-> ", end="")
    for j in i:
        print(j, end=" ")
print("=", minpath)