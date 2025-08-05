def p(g):
    A=[r[:]for r in g];h=len(g);w=len(g[0]);P1=P2=(0,[])
    for i in range(h):
     for j in range(w):
      if g[i][j]:
       q=[(i,j)];g[i][j]=0;pal={A[i][j]};pts=[]
       while q:
        x,y=q.pop();pts+=[(x,y)]
        for a in(-1,0,1):
         for b in(-1,0,1):
          if a|b:
           u,v=x+a,y+b
           if 0<=u<h and 0<=v<w and g[u][v]:
            g[u][v]=0;q+=[(u,v)];pal|={A[u][v]}
       l=len(pal)
       if l>P1[0]:P1=(l,pts)
       if P2[0]==0 or l<P2[0]:P2=(l,pts)
    p1,p2=P1[1],P2[1];c=A[p2[0][0]][p2[0][1]]
    x,y=zip(*p2);mi,ma=min(x),max(x);mj,mz=min(y),max(y)
    bg=[r[mj:mz+1]for r in A[mi:ma+1]];h2=len(bg);w2=len(bg[0])
    x,y=zip(*p1);n1,miny=min(x),min(y);h1=max(x)-n1+1;w1=max(y)-miny+1;si=h2//h1;sj=w2//w1
    out=[[bg[i*si][j*sj]for j in range(w1)]for i in range(h1)]
    for x,y in p1:
     i=x-n1;j=y-miny
     if out[i][j]==c:out[i][j]=A[x][y]
    return out
