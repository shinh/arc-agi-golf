def p(g):
    A=[r[:]for r in g];h=len(g);w=len(g[0]);p=s=[];S=0;T=99
    for i in range(h):
     for j in range(w):
      if g[i][j]:
       R=[(i,j)];g[i][j]=0;P={A[i][j]}
       for x,y in R:
        for a in-1,0,1:
         for b in-1,0,1:
          u,v=x+a,y+b
          if a|b and 0<=u<h and 0<=v<w and g[u][v]:
           g[u][v]=0;R+=[(u,v)];P|={A[u][v]}
       l=len(P)
       if l>S:S=l;p=R
       if l<T:T=l;s=R
    m=A[s[0][0]][s[0][1]];x,y=zip(*s);u,v=min(x),min(y);H=max(x)-u+1;W=max(y)-v+1
    x,y=zip(*p);a,c=min(x),min(y);b=max(x)-a+1;d=max(y)-c+1
    o=[[A[u+i*H//b][v+j*W//d]for j in range(d)]for i in range(b)]
    for x,y in p:
     i=x-a;j=y-c
     if o[i][j]==m:o[i][j]=A[x][y]
    return o
