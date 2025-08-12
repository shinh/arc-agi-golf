# flood fill using rot90 so we only flow to the right
def p(g):
 H=len(g);W=len(g[0]);f=lambda g,n=64:n and f([[a or(b==8 and 8)for a,b in zip(r,r[1:]+(1,))]for r in zip(*g[::-1])],n-1)or g
 for y in range(H):
  for x in range(W):
   if g[y][x]<1:
    g[y][x]=8;g=f(g)
    Y=[i for i,r in enumerate(g)if 8 in r];X=[i for i,r in enumerate(zip(*g))if 8 in r]
    h=Y[-1]-Y[0]+1;w=X[-1]-X[0]+1
    c=[0,[7,2][h%2<1]][Y[0] and X[0] and Y[-1]<H-1 and X[-1]<W-1 and h*w==sum(v>7 for r in g for v in r)]
    g=[[c if v>7 else v for v in r]for r in g]
 return g
