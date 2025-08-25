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

p=lambda g,r=range(10):[[g[y][x]-sum(sum(k[x-1:x+2])for k in g[y-1:y+2])//45*3for x in r]for y in r]
