# 128 zero tile when identical
# def p(g):
#  for r,a,b in zip(g,g[-1:]+g,g[1:]+g):
#   for x,v in enumerate(r):r[x]-=(v==a[x]==b[x])*(r[x-1:x+2]==[v]*3)*v
#  return g

# def p(g):
#     for y in range(1,len(g)-1):
#         for x in range(1,len(g[y])-1):
#             if g[y-1][x-1]==g[y-1][x]==g[y][x-1]==g[y][x]: g[y][x]=0
#     return g

# 109
# def p(g):
#  for a,b in zip(g,g[1:]):
#   for x in range(len(a)):b[x]*=len({*b[x-1:x+1]+a[x-1:x+1]})!=1
#  return g

# 99
# def p(g):
#     for a,b in zip(g,g[1:]):
#         if a==b:
#             for x in range(len(a)-1):b[x+1]*=b[x]<1
#     return g

# 86
def p(g):
    for a,b in zip(g,g[1:]):
        if a==b:
            b[b[::2]>b[1::2]::2]=g[0][::2]
    return g
