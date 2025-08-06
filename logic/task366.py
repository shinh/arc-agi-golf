def p(g):
 h,w=len(g),len(g[0])
 if sum(len({*R})<2 for R in g)>sum(len({*C})<2 for C in zip(*g)):B=g[:h//2];O=g[(h+1)//2:]
 else:B=[R[:w//2]for R in g];O=[R[(w+1)//2:]for R in g]
 F=sum(B,[]);G=sum(O,[])
 if len({*F})>len({*G}):B,O,F,G=O,B,G,F
 B=[*map(list,B)]
 d=max(F,key=F.count)
 e=max(G,key=G.count);G=[v for v in G if v-e]
 if not G:return B
 f=max(G,key=G.count)
 H,W=len(B),len(B[0]);P=[p:=[d]*(W+2)]+[[d]+R+[d]for R in B]+[p]
 h,w=len(O),len(O[0])
 for i in range(h):
  for j in range(w):
   if O[i][j]-e:
    q=[(i,j)];o=[]
    while q:
     x,y=q.pop()
     if 0<=x<h and 0<=y<w and O[x][y]-e:
      o.append((v:=O[x][y],(x,y)));O[x][y]=e
      q+=(x+1,y),(x-1,y),(x,y+1),(x,y-1)
    if not o:continue
    X,Y=zip(*(p for _,p in o));r,R=min(X),max(X);c,C=min(Y),max(Y)
    u=R-r+3;V=C-c+3
    p=[[d]*V for _ in range(u)]
    for v,(x,y) in o:
     if v-f:p[x-r+1][y-c+1]=v
    S={(i-1,j-1)for i in range(H+3-u)for j in range(W+3-V)if all(P[i+a][j+b]==p[a][b]for a in range(u)for b in range(V))}
    if S:
     i,j=next(iter(S));di,dj=i-r+1,j-c+1

     for v,(x,y) in o:
      x+=di;y+=dj
      if 0<=x<H and 0<=y<W:B[x][y]=v
 return B
