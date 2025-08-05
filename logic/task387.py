def p(g):
 h=len(g);w=len(g[0]);o=[r[:] for r in g];t=[];S=set();a=h;b=0;c=w;d=0
 for y in range(h):
  for x in range(w):
   k=g[y][x]
   if k:
    g[y][x]=0;s=[(y,x)];r=[]
    while s:
     i,j=s.pop();r+=[(i,j)];S.add((i,j));a=min(a,i);b=max(b,i);c=min(c,j);d=max(d,j)
     for ny,nx in(i+1,j),(i-1,j),(i,j+1),(i,j-1):
      if 0<=ny<h and 0<=nx<w and g[ny][nx]==k:
       g[ny][nx]=0;s+=[(ny,nx)];r+=s[-1:]
    t+=[(k,r)]
 A,B=sorted({c for c,_ in t})
 for k,r in t:
  oc=[A,B][k==A]
  ys,xs=zip(*r);y0=max(0,min(ys)-1);y1=min(h-1,max(ys)+1);x0=max(0,min(xs)-1);x1=min(w-1,max(xs)+1)
  for j in range(x0,x1+1):o[y0][j]=o[y1][j]=oc
  for i in range(y0,y1+1):o[i][x0]=o[i][x1]=oc
 for i in range(a,b+1):
  for j in range(c,d+1):
   if (i in(a,b) or j in(c,d)) and (i,j) not in S and min(abs(i-y)+abs(j-x) for y,x in S)%2<1:o[i][j]=5
 return o
