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
# def p(g):
#     X=[[0]*6for _ in g+g]
#     i=54
#     while i:=i-1:
#         x=i%3
#         y=i//3%3
#         j=i//9
#         if x<6-i>y: X[y+i][x+i] |= g[y][x]
#     return X
#
# def p(g):
#     a=[g[0][0],g[1][1],g[2,2],
#        g[1][0],g[2][1],
#        g[2][0]
#        g[0][2]
#     return [[max(a[x-y])for x in range(6)]for y in range(6)]

# def p(g):
#     r=range(6)
#     X=[[0]*6for _ in r]
#     for i in range(1,6):
#         for y in range(3):
#             X[i+y][i]=X[i+y-1][i-1]
#     return X

# 112
# def p(g,s=[[0]*9]):
#     for i in range(5):
#         g = [[*map(max,zip(r1+[0],[0]+r2))][:6]for r1,r2 in zip(g+s,s+g)][:6]
#     return g

# 101
p=lambda g,i=-5,s=[[0]*9]: g*i or p([[*map(max,zip(r1+[0],[0]+r2))][:6]for r1,r2 in zip(g+s,s+g)][:6],i+1)