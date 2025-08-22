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
          if a|b and-1<(r:=x+a)<h and-1<(c:=y+b)<w and(k:=g[r][c]):
           g[r][c]=0;R+=(r,c,k),;P|={k};I=min(I,r);K=max(K,r);J=min(J,c);L=max(L,c)
       if(l:=len(P))>S:S=l;p=R;a,c=I,J;b=K-I+1;d=L-J+1
       if l<T:T=l;s=R;u,v=I,J;U=K-I+1;V=L-J+1
    o=[[(i*U//b,j*V//d)in{(x-u,y-v)for x,y,_ in s}for j in range(d)]for i in range(b)]
    for x,y,k in p:o[x-a][y-c]*=k
    return o
