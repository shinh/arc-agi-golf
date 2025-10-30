# # 198 (want 103)
# def p(g):
#  t=[]
#  for r in range(15):
#   for c in range(15):
#    if g[r][c]==g[r+1][c]==g[r][c+1]==g[r+1][c+1]>0:t+=g[r][c],
#  v=max(t,key=t.count);o=[[0]*16for _ in g]
#  for r in range(15):
#   for c in range(15):
#    if g[r][c]==g[r+1][c]==g[r][c+1]==g[r+1][c+1]==v:
#     o[r][c]=o[r][c+1]=o[r+1][c]=o[r+1][c+1]=v
#  return o

# doesn't work, there are some with a 2x2 square of another color
# def p(g):
#     h=[[0]*16for _ in g]
#     for r in range(15):
#         for c in range(15):
#             if g[r][c]==g[r+1][c]==g[r][c+1]==g[r+1][c+1]:
#                 h[r][c]=h[r+1][c]=h[r][c+1]=h[r+1][c+1]=g[r][c]
#     return h

# def p(g):
#     for xs in range(15,1,-1):
#         for ys in range(15,1,-1):
#             for y in range(13):
#                 for x in range(13):
#                     o=[[0]*16for _ in g]
#                     for dy in range(y,min(y+ys,15)):
#                         o[dy][x:x+xs]=g[dy][x:x+xs]
#                     s={*sum(o,[])}
# #                     s={*sum(r[x:x+xs] for r in g[y:y+ys],[])}
#                     if len(s)==2:
#                         return o
#
#
# def p(g):
#     h=[[0]*16for _ in g]
#     gt=[*zip(*g)]
#     for r in range(15):
#         for c in range(15):
#             z=g[r][c]
#             if g[r][c:].index(z)+g[r][:c:-1].index(z)+gt[c][r:].index(z)+gt[c][:r:-1].index(z)>5:
#                 h[r][c]=z
#     return h

def p(g):
    h=[[0]*16for _ in g]
    for b in [2,3]:
        b3=5-b
        for y in range(15):
            for x in range(15):
#                 if z and [r[x:x+b] for r in g[y:y+b3]]==[[z]*b]*b3:
#                 if z and [*zip(*g[y:y+b3])][x:x+b]==[(z,)*b3]*b:
                for dy in range(b3*([r[x:x+b] for r in g[y:y+b3]]==[[g[y][x]]*b]*b3)):
                    h[y+dy][x:x+b]=[g[y][x]]*b
    return h