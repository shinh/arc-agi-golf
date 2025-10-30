def p(g):
 y,x=zip(*((i,j)for i,r in enumerate(g)for j,v in enumerate(r)if v==4));A,B=min(y),max(y);C,D=min(x),max(x);b=[r[C:D+1]for r in g[A:B+1]]
 y,x=zip(*((i,j)for i,r in enumerate(g)for j,v in enumerate(r)if(i<A or i>B or j<C or j>D)and v&-5));e,f=min(y),max(y);h,k=min(x),max(x)
 for z in range(2,5):
  H,W=(f-e+1)*z,(k-h+1)*z
  for u in range(len(b)-H+1):
   for v in range(len(b[0])-W+1):
    if all(0<=i-u<H and 0<=j-v<W and t==g[e+(i-u)//z][h+(j-v)//z]for i,r in enumerate(b)for j,t in enumerate(r)if t&-5):
     for i in range(H):
      for j in range(W):b[u+i][v+j]=b[u+i][v+j]or g[e+i//z][h+j//z]
     return b
 return b
