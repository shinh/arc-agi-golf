# 155
# def p(g):
#  def f(x,y):
#   try:
#    if g[y][x]<2:g[y][x]=2;f(x,y+1);f(x,y-1);f(x+1,y);f(x-1,y)
#   except:0
#  f(0,0);f(0,-1)
#  return [[0**v*3for v in r]for r in g]

# 133
# def p(g):
#     g2=[]
#     for r in g:
#         r2 = []
#         p = 0
#         c = 0
#         for v in r:
#             c ^= v == 2
#             if p and v: c = 0
#             r2+=[(not v and c)*3]
#             p=v
#         g2+=[r2]
#     return g2

# c v p  new c
# 0 0 0  0
# 0 0 1  0
# 0 1 0  1
# 0 1 1  0
# 1 0 0  1
# 1 0 1  1
# 1 1 0  0
# 1 1 1  0

# # 109
# def p(g):
#     g2=[]
#     for r in g:
#         r2 = []
#         p = 0
#         c = 0
#         for v in r:
#             c=(c^v)*0**(p*v)
#             r2+=[(c>v)*3]
#             p=v
#         g2+=[r2]
#     return g2


# 93
# def p(g):
#     g2=[]
#     for r in g:
#         p = 0
#         c = 0
#         g2+=[[((c:=(c^v)*0**(p*v))>(p:=v))*3 for v in r]]
#     return g2

# 86 (more improvement with magic formulas still possible probably)
# p=lambda g,q=0,c=0:[[((c:=(c^v)*0**(q*v))>(q:=v))*3for v in g[0]]]+(g[1:]and p(g[1:]))

# 85
# def p(g):
#     for r in g:
#         p=c=0
#         r[:]=[((c:=(c^v)*0**(p*v))>(p:=v))*3 for v in r]
#     return g

# 82
# p=lambda g,q=0,c=0:[[((c:=(c^v)*0**(q*v))>(q:=v))*3 for v in r+[0]][:-1]for r in g]

# 77
# p=lambda g,c=0:[(q:=0)or[((c:=(c^v)*0**(q*v))>(q:=v))*3 for v in r]for r in g]

p=lambda g,c=0:[[((c:=(c^v)*0**(q*v))>v)*3 for v,q in zip(r,[0]+r)]for r in g]

# other (not working ideas):...

# def p(g):
#     og=[r*1 for r in g]
#     for y in range(1,len(g)):
#         for x in range(1,len(g)):
#             if og[y-1][x] and og[y][x-1] and not g[y][x]: og[y][x]=g[y][x]=3
#             else: g[y][x]=0
#     return g

# idea
# make all blacks green then flood fill black+red (don't add neighbors if red)

# idea
# # test cases are all rectangles so just replace red black* red with green*
# doesn't handle solid lines and multiple per line
# def p(g):
#     for r in g:
#         p=1
#         f=0
#         for x,v in enumerate(r):
#            if f%2 and v and p: f+=1
#            if p==0 and v: f+=1
#            if f%2 and not v: r[x]=3
#            else: r[x]=0
#            p=v
#     return g

# idea
# def p(g):
#     c=0
#     return [[3 if (c:=c+v)==2 and not v else 0 for v in r]for r in g]

# idea regex
# import re
# def p(g):
#     return [for r in g]

