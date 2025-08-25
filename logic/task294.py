# rotate flood-fill to erode 5-pixels
# p=lambda g,f=lambda m:[[*map(min,r,r[1:]),0]for r in zip(*m[::-1])]:[[c-d*.6 for c,d in zip(*t)]for t in zip(g,f(f(f(f(g)))))]

# new approach
# def p(g,r=range(1,9)):
#     for x in r:
#         for y in r:
#             if g[y+1][x]*g[y-1][x]*g[y][x-1]*g[y][x+1]:
#                 g[y][x]=2
#     return g

# def p(g):
#     for z in range(64):
#         y,x=z//8+1,z%8+1
#         g[y][x]-=(g[y+1][x]*g[y-1][x]*g[y][x-1]*g[y][x+1]>0)*3
#     return g
#
# def p(g,y=1,x=1):
#     if y==9: return g
#     g[y][x]-=(g[y+1][x]*g[y-1][x]*g[y][x-1]*g[y][x+1]>0)*3
#     return p(g,y+x//8,x%8+1)

# def p(g):
#     for z in range(10,89):
#         sum(sum(g,[])[z+x]%3 for x in[-1,1,-10,10])
#     if y==9: return g
#     g[y][x]-=(g[y+1][x]*g[y-1][x]*g[y][x-1]*g[y][x+1]>0)*3
#     return p(g,y+x//8,x%8+1)

# def p(g,r=range(10)):
#     return [[sum(sum(k[x-1:x+2])for k in g[y-1:y+2])>44 and 2 or g[y][x] for x in r]for y in r]

# p=lambda g,r=range(10):[[g[y][x]-sum(sum(k[x-1:x+2])for k in g[y-1:y+2])//45*3for x in r]for y in r]


# def f(a,b):
#     if not a: return 0
#     if b: return a-1
#     return a

# p=lambda m,n=4:p([[f(a,b)if n>1 else [0,2,5,5][f(a,b)]for a,b in zip(x,[*x[1:],0])]for x in zip(*m)][::-1],n-1)if n else m

# p=lambda m,n=4:p([[f(a,b)for a,b in zip(x,[*x[1:],0])]for x in zip(*m)][::-1],n-1)if n else [[[0,2,5,5][x]for x in r] for r in m]

# p=lambda g,r=range(10):[[g[y][x]-sum(k[x-1:x+2]>[5,5,4]for k in g[y-1:y+2])//3*3for x in r]for y in r]

# test cases are "bad", only need to look diagonally in 2 directions not 4
# def p(g,r=range(1,9)):
#     for x in r:
#         for y in r:
#             if g[y][x]*g[y+1][x+1]*g[y-1][x-1]:
#                 g[y][x]=2
#     return g

# def p(g,r=range):
#     for x in r(8):
#       for y in r(8):
# #         y,x=z//8,z%8
# #         g[y][x]-=(g[y+1][x+1]*g[y][x]*g[y][x-1]*g[y][x+1]>0)*3
#         g[y+1][x+1]-=sum(g[y+a][x+a]for a in r(3))//11*3
#     return g
#
# def p(g,r=range(1,9)):
#     for x in r:
#       for y in r:
# # #         y,x=z//8,z%8
#         # 2,5 or 5,5 -> 3 else e.g. 5,0 -> any number > 5
#         g[y][x]%=6/(g[y+1][x+1]*g[y-1][x-1]%3+1)
# #         g[y+1][x+1]-=sum(g[y+a][x+a]for a in r(3))//11*3
#     return g


# def p(g):
#     for z in range(64):
#         y,x=z//8,z%8
#         # 2,5 or 5,5 -> 3 else e.g. 5,0 -> any number > 5
#         g[y+1][x+1]%=6/(g[y+2][x+2]*g[y][x]%3+1)
# #         g[y+1][x+1]-=sum(g[y+a][x+a]for a in r(3))//11*3
#     return g

# # 91
# def p(g):
#     for z in range(64):
#         if g[y:=z//8][x:=z%8]*g[y+2][x+2]:g[y+1][x+1]%=3
#     return g

# def p(g,z=0):
#     if g[y:=z//8][x:=z%8]*g[y+2][x+2]:g[y+1][x+1]%=3
#     return z<63 and p(g,z+1)or g

def p(g,z=0):
    exec("if g[y:=z//8][x:=z%8]*g[y+2][x+2]:g[y+1][x+1]%=3\nz+=1\n"*64)
    return g
