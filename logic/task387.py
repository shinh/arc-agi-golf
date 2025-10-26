def p(g):
 p=[(i,j,x)for i,r in enumerate(g)for j,x in enumerate(r)if x];a,c,_=min(p);b,d,_=max(p)
 for i,j,x in p:
  t=g[a][c]+g[a][d]-x;g[i-1][j-1:j+2]=g[i+1][j-1:j+2]=[t]*3;g[i][j-1:j+2]=[t,x,t]
 for L in range(2,(d-c)//2+1,2):g[a][c+L]=g[a][d-L]=g[b][c+L]=g[b][d-L]=5
 for L in range(2,(b-a)//2+1,2):g[a+L][c]=g[b-L][c]=g[a+L][d]=g[b-L][d]=5
 return g