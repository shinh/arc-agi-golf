# move patterns from one half onto the other
def p(g):
 h=len(g);w=len(g[0])
 if sum(len({*r})<2 for r in g)>sum(len({*c})<2 for c in zip(*g)):B,O=g[:h//2],g[(h+1)//2:]
 else:B,O=[r[:w//2]for r in g],[r[(w+1)//2:]for r in g]
 F=sum(B,[]);G=sum(O,[])
 if len({*F})>len({*G}):B,O,F,G=O,B,G,F
 d=max(F,key=F.count);e=max(G,key=G.count)
 H,W=len(B),len(B[0]);P=[p:=[d]*(W+2)]+[[d]+r+[d]for r in B]+[p]
 if not(G:=[v for v in G if v-e]):return B
 f=max(G,key=G.count);h,w=len(O),len(O[0])
 for i in range(h):
    for j in range(w):
     if O[i][j]-e:
      q=[(i,j)];o=[]
      while q:
       x,y=q.pop()
       if 0<=x<h and 0<=y<w and O[x][y]-e:
        v=O[x][y];O[x][y]=e;o+=[(v,x,y)];q+=(x+1,y),(x-1,y),(x,y+1),(x,y-1)
      _,X,Y=zip(*o);r=min(X);R=max(X);c=min(Y);C=max(Y);u=R-r+3;V=C-c+3
      p=[[d]*V for _ in range(u)]
      for v,x,y in o:
       if v-f:p[x-r+1][y-c+1]=v
      S={(I-1,J-1)for I in range(H+3-u)for J in range(W+3-V)if all(P[I+a][J+b]==p[a][b]for a in range(u)for b in range(V))}
      if S:
       I,J=next(iter(S));di,dj=I-r+1,J-c+1
       for v,x,y in o:
        x+=di;y+=dj
        if 0<=x<H and 0<=y<W:B[x][y]=v
 return B

