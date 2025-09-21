# 428
# def p(g):
#     h,w=len(g),len(g[0]);R=[*map(list,g)];r=range
#     def F(i,j):
#         if-1<i<h and-1<j<w and(u:=g[i][j])>0:
#             g[i][j]=0;return[(i,j,u)]+F(i+1,j)+F(i-1,j)+F(i,j+1)+F(i,j-1)
#         return[]
#     for i in r(h):
#         for j in r(w):
#             if g[i][j]:
#                 C=F(i,j);x,y,z=zip(*C)
#                 if len({*z})>3:
#                     a,b,c,d=min(x),max(x)+1,min(y),max(y)+1
#                     P=[(x-a,y-c,u)for x,y,u in C]
#                     for x,y,_ in C:R[x][y]=0
#                     m=max(z,key=z.count);H=b-a;W=d-c
#                     for _ in'00':
#                         for _ in'0000':
#                             for I in r(h-H+1):
#                                 for J in r(w-W+1):
#                                     if all(u==m or R[I+x][J+y]==u for x,y,u in P):
#                                         for x,y,u in P:R[I+x][J+y]=u
#                             H1=H;P=[(y,H1-1-x,u)for x,y,u in P];H,W=W,H1
#                         P=[(H-1-x,y,u)for x,y,u in P]
#     return R

# gather larger objects and erase them
# for each large object
    # try all placements
        # if matches, then accept

# 370
# def rm(g,y,x):
#     if 0<=y<len(g) and 0<=x<len(g[0]) and g[y][x]:
#         point = (y,x,g[y][x])
#         g[y][x] = 0
#         return [point] + rm(g,y+1,x)+rm(g,y-1,x)+rm(g,y,x+1)+rm(g,y,x-1)
#     else:
#         return []
#
# def rm2(g,y,x): # non recursive version of rm, can be inlined
#     q = [(y,x)]
#     ret = []
#     for y,x in q:
#         if 0<=y<len(g) and 0<=x<len(g[0]) and g[y][x]:
#             ret += [(y,x,g[y][x])]
#             g[y][x] = 0
#             q+=[(y+1,x),(y-1,x),(y,x+1),(y,x-1)]
#     return ret
#
# def draw(g,obj):
#     for y,x,c in obj:
#         g[y][x] = c
#
# def maybe_draw(g,obj):
#     _,_,cs = zip(*obj)
#     mode = max(cs,key=cs.count)
#     if all(0<=y<len(g) and 0<=x<len(g[0]) and c in (mode,g[y][x]) for y,x,c in obj): draw(g,obj)
#
# def p(g):
#     objects=[]
#     for h in range(-20,20):
#         for w in range(-20,20):
#             obj = rm2(g,h,w)
#             if len(obj) < 4: draw(g,obj)
#             else: objects += [obj]
#
#     for i in range(8):
#         if i%4: g = g[::-1]
#         g = [*map(list,zip(*g))]
# #         g = [*map(list,zip(*g[::i%4//3*2-1]))]
#         for obj in objects:
#             for dy in range(-20,20):
#                 for dx in range(-20,20):
#                     maybe_draw(g, [(y+dy,x+dx,c) for y,x,c in obj])
#     return g



# 344
def p(g):#
    objects=[]
    for y in range(-20,20):
        for x in range(-20,20):
            q = [(y,x)]
            obj = []
            for y,x in q:
                if 0<=y<len(g) and 0<=x<len(g[0]) and g[y][x]:
                    obj += [(y,x,g[y][x])]
                    g[y][x] = 0
                    q+=[(y+1,x),(y-1,x),(y,x+1),(y,x-1)]

            if len(obj) < 4:
                for y,x,c in obj:
                    g[y][x] = c
            else: objects += [obj]

    for i in range(8):
        g = [*map(list,zip(*g[::i%4//3*2-1]))]
        for obj2 in objects:
            for dy in range(-20,20):
                for dx in range(-20,20):
                    obj = [(y+dy,x+dx,c) for y,x,c in obj2]
                    _,_,cs = zip(*obj)
                    mode = max(cs,key=cs.count)
                    if all(0<=y<len(g) and 0<=x<len(g[0]) and c in (mode,g[y][x]) for y,x,c in obj):
                        for y,x,c in obj:
                            g[y][x] = c

    return g

