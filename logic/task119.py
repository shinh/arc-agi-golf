def p(g):
 h=12;A=[];P=[]
 for i in range(h):
  for j,v in enumerate(g[i]):
   if v==8:A+=[(i,j)]
   elif v==2:P+=[(i,j)]
 r,c=zip(*P);R=min(r);B=max(r);C=min(c);D=max(c)
 r8,c8=map(min,zip(*A))
 d=lambda i,j:max(C-j,0,j-D)+max(R-i,0,i-B)
 t=min(A,key=lambda p:d(*p))
 s=1 if (r8,c8) in A else -1
 e=(1,s);f=(-1,-s)
 if d(t[0]+e[0],t[1]+e[1])>d(t[0]+f[0],t[1]+f[1]):e=f
 a,b=e;i,j=t
 while not(R-1<=i<=B+1 and C-1<=j<=D+1 and (i in (R-1,B+1) or j in (C-1,D+1))):i+=a;j+=b
 if B-R+1==h:s=1 if c8>C else -1;T=(1,s),(-1,s)
 else:s=1 if r8>R else -1;T=(s,1),(s,-1)
 for di,dj in T:
  x,y=i,j
  while 0<=x<h and 0<=y<h:
   if g[x][y]!=8:g[x][y]=3
   x+=di;y+=dj
 return g

