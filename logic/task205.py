# Just solved.
#
# Based on 338. See also 029
#
# crop big blob then stretch the rare color as a cross
def p(g):
    for sy in range(len(g)):
        for sx in range(len(g[0])):
            for ey in range(len(g),sy+2,-1):
                for ex in range(len(g[0]),sx+2,-1):
                    if{g[sy][sx]}=={*g[sy][sx:ex],*g[ey-1][sx:ex],*[g[y][x]for y in range(sy,ey)for x in(sx,ex-1)]}:
                        g=[[g[y][x]for x in range(sx,ex)]for y in range(sy,ey)]
                        c=pts=[]
                        for y in range(len(g)):
                            for x in range(len(g[0])):
                                if g[y][x]!=g[0][0]:
                                    c=g[y][x]
                                    for i in range(len(g)):
                                        pts.append((i,x))
                                    for j in range(len(g[0])):
                                        pts.append((y,j))
                        for i,j in pts:
                            g[i][j]=c
                        return g

# def p(g):
#     h=len(g);w=len(g[0]);v=set();B=[];C=0
#     for i in range(h):
#         for j in range(w):
#             if(i,j)in v:continue
#             c=g[i][j];q=[(i,j)];v.add((i,j));t=[]
#             while q:
#                 x,y=q.pop();t.append((x,y))
#                 for a,b in(1,0),(-1,0),(0,1),(0,-1):
#                     u,vv=x+a,y+b
#                     if 0<=u<h and 0<=vv<w and g[u][vv]==c and(u,vv)not in v:v.add((u,vv));q.append((u,vv))
#             if len(t)>len(B):B=t;C=c
#     rs=[r for r,_ in B];cs=[c for _,c in B]
#     g=[row[min(cs):max(cs)+1]for row in g[min(rs):max(rs)+1]]
#     for _ in range(32):
#         g=[list(r)for r in zip(*g[::-1])]
#         if len(g[0])-2>g[0].count(C):g=g[1:]
#     H=len(g);W=len(g[0]);f=sum(g,[]);d=min(set(f),key=f.count)
#     P=[(i,j)for i,r in enumerate(g)for j,v in enumerate(r)if v==d]
#     for i,j in P:
#         for k in range(H):g[k][j]=d
#         for k in range(W):g[i][k]=d
#     return g

# Following did not work. Finding the rectangle during cropping is hard.
#
# def p(g):
#     show(g,"in")
#     f=sum(g,[])
#     c=max(f,key=f.count)
#     for i in range(120):
#         m=max(r.count(c)for r in g)
#         if(g[0]+g[1]+g[2]).count(c)<m*3-4or g[0].count(c)<=m//2:g=g[1:]
#         g=[*map(list,zip(*g[::-1]))]

#     if len(set(sum(g,[])))!=2:
#         show(g,"hm")

#     print("OK")

#     assert len(set(sum(g,[])))<=2

#     pts=[(i,j)for i,r in enumerate(g)for j,v in enumerate(r)if v!=c]
#     H=len(g);W=len(g[0])
#     for i,j in pts:
#         for k in range(H):g[k][j]=g[i][j]
#         for k in range(W):g[i][k]=g[i][j]
#     return g
