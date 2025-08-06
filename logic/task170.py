def p(g):
    A=[r[:]for r in g];h=len(g);w=len(g[0]);p=s=[];S=0;T=99
    for i in range(h):
     for j in range(w):
      if g[i][j]:
       R=[(i,j)];g[i][j]=0;P={A[i][j]};I=K=i;J=L=j
       for x,y in R:
        for a in-1,0,1:
         for b in-1,0,1:
          r,c=x+a,y+b
          if a|b and 0<=r<h and 0<=c<w and g[r][c]:
           g[r][c]=0;R+=(r,c),;P|={A[r][c]};I=min(I,r);K=max(K,r);J=min(J,c);L=max(L,c)
       if(l:=len(P))>S:S=l;p=R;a=I;b=K;c=J;d=L
       if l<T:T=l;s=R;u=I;U=K;v=J;V=L
    U-=u-1;V-=v-1;b-=a-1;d-=c-1;D={(x-u,y-v):A[x][y]for x,y in s}
    o=[[D.get((i*U//b,j*V//d),0)for j in range(d)]for i in range(b)]
    for x,y in p:
     i,j=x-a,y-c
     if o[i][j]:o[i][j]=A[x][y]
    return o
