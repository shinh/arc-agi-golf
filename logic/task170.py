def p(g):
    # scale smallest region to largest and overlay
    h=len(g);w=len(g[0]);p=s=[];S=0;T=9
    for i in range(h):
     for j in range(w):
      if k:=g[i][j]:
       R=[(i,j,k)];g[i][j]=0;P={k};I=K=i;J=L=j
       for x,y,_ in R:
        for a in-1,0,1:
         for b in-1,0,1:
          r,c=x+a,y+b
          if a|b and-1<r<h and-1<c<w and(k:=g[r][c]):
           g[r][c]=0;R+=(r,c,k),;P|={k};I=min(I,r);K=max(K,r);J=min(J,c);L=max(L,c)
       if(l:=len(P))>S:S=l;p=R;a,b,c,d=I,K,J,L
       if l<T:T=l;s=R;u,U,v,V=I,K,J,L
    U-=u-1;V-=v-1;b-=a-1;d-=c-1;D={(x-u,y-v):k for x,y,k in s}
    o=[[D.get((i*U//b,j*V//d),0)for j in range(d)]for i in range(b)]
    for x,y,k in p:o[x-a][y-c]=o[x-a][y-c]and k
    return o
