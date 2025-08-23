def p(g):
    # shrink first region to leftover
    h=len(g);w=len(g[0])
    for y in range(h):
     for x in range(w):
      if k:=g[y][x]:
       r=[(y,x)];g[y][x]=0;u=U=y;v=V=x
       for i,j in r:
        u=min(u,i);U=max(U,i);v=min(v,j);V=max(V,j)
        for a in-1,0,1:
         for b in-1,0,1:
          if a|b and-1<(p:=i+a)<h and-1<(q:=j+b)<w and g[p][q]==k:
           g[p][q]=0;r+=(p,q),
       break
     else:continue
     break
    U-=u-1;V-=v-1;t={(i-u,j-v)for i,j in r}
    A=h;B=D=0;C=w
    for i in range(h):
     for j in range(w):
      if v:=g[i][j]:A=min(A,i);B=max(B,i);C=min(C,j);D=max(D,j)
    B-=A-1;D-=C-1
    return [[g[i][j]*(((i-A)*U//B,(j-C)*V//D)in t)for j in range(C,C+D)]for i in range(A,A+B)]
