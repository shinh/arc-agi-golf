# # ungolfed, 304
# def p(g):
#     ds=3,4
#     been=set()
#     while 1: # can also do while 1
#         a=[]
#         for y,row in enumerate(g):
#             for x,_ in enumerate(row):
#                 for l in ds:
#                     points=set()
#                     for d in range(-l+1,l):
#                         yy=y+d
#                         if 0<=yy<len(g):
#                             points.add((yy,x))
#                         xx=x+d
#                         if 0<=xx<len(g[0]):
#                             points.add((y,xx))
#                     points-=been
#                     colors = [g[yy][xx] for yy,xx in points]
#                     if colors.count(0) == 0:
#                         count = colors.count(2)
#                         # prioritize covering reds, then reducing diameter (when sorted)
#                         a+=[(-count,l,points)]
#         count,d,points=min(a)
#         ds=[d] # set diameter for all next crosses
#         if count==0: break
#         for y,x in points: g[y][x]+=g[y][x]-2 # 5 -> 8, 2 -> 2
#         been|=points
#     return g

# golfed, 262
def p(g,ds=[3,4],been={1},*a):
    # could use a list comprehension for a, but python weird about using := inside it so not sure if possible
    for y in range(len(g)):
        for x in range(len(g[0])):
            for l in ds:
                points = ({(z,x) for z in range(y-l+1,y+l) if 0<=z<len(g)}|{(y,z) for z in range(x-l+1,x+l) if 0<=z<len(g[0])})-been

                colors = [g[yy][xx] for yy,xx in points]
                a+=(-colors.count(2)*all(colors),l,points),
    count,*ds,points=min(a)
    for y,x in points: g[y][x]+=g[y][x]-2 # 5 -> 8, 2 -> 2
    points and p(g,ds,been|points)
    return g