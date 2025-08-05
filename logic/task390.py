def p(g):
 h=w=15
 c=[(i,j)for i in range(h)for j in range(w)if g[i][j]==2]
 a=min(i for i,j in c);b=max(i for i,j in c);l=min(j for i,j in c);r=max(j for i,j in c)
 sub=[row[l:r+1] for row in g[a:b+1]]
 t=any(len(set(row))==1 for row in sub)
 if t:g=[list(x)for x in zip(*g)];h,w=w,h
 c=[(i,j)for i in range(h)for j in range(w)if g[i][j]==2]
 a=min(i for i,j in c);b=max(i for i,j in c);l=min(j for i,j in c);r=max(j for i,j in c)
 o=[row[:] for row in g]
 for i in range(a+1,b):
  for j in range(l+1,r):o[i][j]=0
 inner=[row[l+1:r] for row in g[a+1:b]]
 if inner and inner[0]:
  m=len(inner[0])//2
  L=[row[:m][::-1] for row in inner]
  R=[row[m:][::-1] for row in inner]
  for i,row in enumerate(L):
   for j,v in enumerate(row):
    if v==5:o[a+1+i][l-m+j]=5
  for i,row in enumerate(R):
   for j,v in enumerate(row):
    if v==5:o[a+1+i][r+1+j]=5
 if t:o=[list(x)for x in zip(*o)]
 return o
