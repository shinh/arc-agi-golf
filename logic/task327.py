# extend diagonals
# 139
# def p(g,e=enumerate):X=[[0]*6for _ in g+g];[X[r+i].__setitem__(c+i,v)for r,R in e(g)for c,v in e(R)for i in range(6-max(r,c))if v];return X

# 136
# def p(g):
#     r=range(6)
#     X=[[0]*6for _ in r]
#     for i in r:
#         for y in r:
#             for x in r:
#                 try:
#                     X[y+i][x+i] |= g[y][x]
#                 except: 0
#     return X

# 121
def p(g):
    X=[[0]*6for _ in g+g]
    i=54
    while i:=i-1:
        x=i%3
        y=i//3%3
        j=i//9
        if x<6-i>y: X[y+i][x+i] |= g[y][x]
    return X

