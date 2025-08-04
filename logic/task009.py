def p(g):
 h=len(g);w=len(g[0])
 R=[i for i in range(h) if len(set(g[i]))==1]
 C=[j for j in range(w) if len({g[i][j]for i in range(h)})==1]
 fr=g[R[0]][0] if R else (g[0][C[0]] if C else 0)
 cnt=[0]*10
 for i in range(h):
  if i in R:continue
  for j in range(w):
   if j in C:continue
   cnt[g[i][j]]+=1
 bg=max(range(10),key=cnt.__getitem__)
 d={}
 for i in range(h):
  if i in R:continue
  for j in range(w):
   if j in C:continue
   c=g[i][j]
   if c!=bg and c!=fr:d.setdefault(c,[]).append((i,j))
 for c,pts in d.items():
  for a in range(len(pts)):
   y1,x1=pts[a]
   for y2,x2 in pts[a+1:]:
    if y1==y2:
     for x in range(min(x1,x2),max(x1,x2)+1):g[y1][x]=c
    elif x1==x2:
     for y in range(min(y1,y2),max(y1,y2)+1):g[y][x1]=c
 for i in R:
  for j in range(w):g[i][j]=fr
 for j in C:
  for i in range(h):g[i][j]=fr
 return g
