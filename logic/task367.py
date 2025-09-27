# if in a black inside corner that doesn't extend make yellow
# if black and yellow neighbor make yellow
# rotate 4x to only check rule in 1 direction
# def p(g,R=range(20)):
#     for _ in R:
#         for y in R:
#             for x in R:
#                 try:
#                     if g[y][x]==0 and g[y+1][x]==4 or g[y][x]==g[y+2][x+1]==g[y+1][x+2]==0 and g[y+1][x]==g[y][x+1]==5:
#                         g[y][x]=4
#                 except:0
#         g = [*map(list,zip(*g[::-1]))]
#     return g

# 202
# def p(g,R=range(20)):
#     for _ in R:
#         t=g[::-1]
#         g = [*map(list,zip(*t))]
#         for y in R:
#             for x in R:
#                 try:
#                     1/(g[y][x:x+2]==[0,4] or t[x+1][y:y+3]== g[y+1][x:x+3]==[5,5,0])
#                     g[y][x]=4
#                 except:0
#     return g

# 181
# def p(g):
#     for i in range(8000):
#         t=g[::-1]
#         g = [*map(list,zip(*t))]
#         x = i % 23
#         y = i % 19
#         try:
#             1/(g[y][x:x+2]==[0,4] or t[x+1][y:y+3]==g[y+1][x:x+3]==[5,5,0])
#             g[y][x]=4
#         except:0
#     return g

# 179
def p(g,i=8000):
    while i:
        i-=1
        t=g[::-1]
        g = [*map(list,zip(*t))]
        x = i % 23
        y = i % 19
        try:
            g[y][x//(g[y][x:x+2]==[0,4] or t[x+1][y:y+3]==g[y+1][x:x+3]==[5,5,0])]=4
        except:0
    return g