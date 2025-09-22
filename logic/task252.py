# def p(g):
#     # use first row/col to draw diagonals
#     r=range(len(g))
#     for x in r[1::2]:
#         for y in r[x:]:
#             if g[0][y-x]:g[x][y]=4
#             if g[y-x][0]:g[y][x]=4
#     return g
#
# 97
# def p(g):
#     for y in(r:=range(len(g)-1)):
#         for x in r:
#             if 0<g[y][x]!=4:
#                 g[y+1][x+1]=4
#     return g
#

# 94
# def p(g,z=0):
#     n=len(g)-1
#     if 0<g[y:=z//n][x:=z%n]!=4: g[y+1][x+1]=4
#     if y<n: p(g,z+1)
#     return g

# 95
# def p(g):
#     for x,v in enumerate(g[0][:-1]):
#         if 0<v!=4:g[1][x+1]=4
#     g[2:]and p(g[1:])
#     return g

# 97
# def p(g,x=0):
#     while(x:=x+1)<len(g[0]):
#         if 0<g[0][x-1]!=4:g[1][x]=4
#     g[2:]and p(g[1:])
#     return g

# 94
# def p(g,x=1):
#     n=len(g[0])-1
#     if 0<g[0][x-1]!=4:g[1][x]=4
#     g[1:]and p(g[x>=n:],x%n+1)
#     return g

# 93
def p(g,z=0):
    n=len(g)-1
    if 0<g[y:=z//n][z%n]!=4: g[y+1][z%n+1]=4
    if y<n: p(g,z+1)
    return g
