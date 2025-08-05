def p(g):
 h,w=len(g),len(g[0])
 if sum(len({*R})<2 for R in g)>sum(len({*C})<2 for C in zip(*g)):a=g[:h//2];b=g[(h+1)//2:]
 else:a=[R[:w//2]for R in g];b=[R[(w+1)//2:]for R in g]
 if len({*sum(a,[])})>len({*sum(b,[])}) :a,b=b,a
 B=[*map(list,a)];O=b
 d=max(F:=sum(B,[]),key=F.count)
 e=max(G:=sum(O,[]),key=G.count);G=[v for v in G if v-e]
 if not G:return B
 f=max(G,key=G.count)
 H,W=len(B),len(B[0]);p=[d]*(W+2);P=[p]+[[d]+R+[d]for R in B]+[p]
 h,w=len(O),len(O[0])
 for i in range(h):
  for j in range(w):
   if O[i][j]-e:
    q=[(i,j)];o=[]
    while q:
     x,y=q.pop()
     if 0<=x<h and 0<=y<w and O[x][y]-e:
      v=O[x][y];O[x][y]=e;o.append((v,(x,y)))
      q+=(x+1,y),(x-1,y),(x,y+1),(x,y-1)
    X,Y=zip(*(p for _,p in o));mi,ma=min(X),max(X);mj,mb=min(Y),max(Y)
    ph=ma-mi+3;pw=mb-mj+3
    p=[[d]*pw for _ in range(ph)]
    for v,(x,y) in o:
     if v-f:p[x-mi+1][y-mj+1]=v
    pi,pj=mi-1,mj-1
    S={(si-1,sj-1)for si in range(H+3-ph)for sj in range(W+3-pw)if all(P[si+a][sj+b]==p[a][b]for a in range(ph)for b in range(pw))}
    if S:
     si,sj=next(iter(S));di,dj=si-pi,sj-pj
     for v,(x,y) in o:
      x+=di;y+=dj
      if 0<=x<H and 0<=y<W:B[x][y]=v
 return B
