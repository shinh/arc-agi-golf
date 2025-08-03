def p(g):
 h=len(g);w=len(g[0]);m=(h+1)//3;n=(w+1)//3;b=[[g[i*3][j*3]for j in range(n)]for i in range(m)]
 for j in range(n):
  i=0
  while i<m:
   c=b[i][j]
   if c:
    k=i+1
    while k<m and b[k][j]==0:k+=1
    if k<m and b[k][j]==c:
     for t in range(i+1,k):b[t][j]=c
    i=k
   else:i+=1
 for r in b:
  j=0
  while j<n:
   c=r[j]
   if c:
    k=j+1
    while k<n and r[k]==0:k+=1
    if k<n and r[k]==c:
     for t in range(j+1,k):r[t]=c
    j=k
   else:j+=1
 for i in range(m):
  for j in range(n):
   c=b[i][j]
   if c:
    y=i*3;x=j*3
    g[y][x]=g[y][x+1]=g[y+1][x]=g[y+1][x+1]=c
 return g
