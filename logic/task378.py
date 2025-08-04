def p(g):
 d={}
 for i,r in enumerate(g):
  for j,v in enumerate(r):
   d.setdefault(v,[i,i,j,j])
   a=d[v]
   a[0]=min(a[0],i);a[1]=max(a[1],i)
   a[2]=min(a[2],j);a[3]=max(a[3],j)
 c=sorted(d,key=lambda k:(d[k][1]-d[k][0]+1)*(d[k][3]-d[k][2]+1),reverse=1)
 a=d[c[1]];t=c[2];h=len(g);w=len(g[0])
 for(s,(di,dj)) in zip([(a[1]+1,a[3]+1),(a[1]+1,a[2]-1),(a[0]-1,a[3]+1),(a[0]-1,a[2]-1)],[(1,1),(1,-1),(-1,1),(-1,-1)]):
  i,j=s
  while 0<=i<h and 0<=j<w:g[i][j]=t;i+=di;j+=dj
 return g
