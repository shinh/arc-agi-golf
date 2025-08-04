def p(g):
 h=len(g);w=len(g[0]);c={}
 for r in g:
  for v in r:c[v]=c.get(v,0)+1
 bg=max(c,key=c.get);c.pop(bg);m=max(c,key=c.get)
 V=set();C=[]
 for i in range(h):
  for j in range(w):
   if g[i][j]!=bg and (i,j)not in V:
    q=[(i,j)];V.add((i,j));t=b=i;l=r=j;n=0
    while q:
     x,y=q.pop();n+=1
     if x<t:t=x
     if x>b:b=x
     if y<l:l=y
     if y>r:r=y
     for dx,dy in((1,0),(-1,0),(0,1),(0,-1)):
      nx,ny=x+dx,y+dy
      if 0<=nx<h and 0<=ny<w and g[nx][ny]!=bg and (nx,ny)not in V:
       V.add((nx,ny));q.append((nx,ny))
    C.append((n,t,b,l,r))
 C.sort();n,t,b,l,r=C.pop()
 o=[row[l:r+1] for row in g[t:b+1]]
 R=[[m]*len(o[0]) for _ in o]
 O=[]
 for n,t,b,l,r in C:
  if (b-t+1)*(r-l+1)!=n:continue
  pch=[row[l:r+1] for row in g[t:b+1]]
  s={v for row in pch for v in row}
  if len(s)==2 and m in s:O.append(pch)
 def tr(p):
  r=[p]
  for _ in'123':
   p=[list(z) for z in zip(*p[::-1])];r+=[p]
  return r+[[row[::-1] for row in q] for q in r]
 H=len(o);W=len(o[0])
 for P in O:
  for t in tr(P):
   ph=len(t);pw=len(t[0]);f=s=None
   for i in range(H-ph+1):
    for j in range(W-pw+1):
     if all((t[a][b]==m)==(o[i+a][j+b]==0) for a in range(ph) for b in range(pw)):
      s=(i,j);f=f or s
   if s:
    i,j=s
    if i*j==0 or i+ph==H or j+pw==W:i,j=f
    for a in range(ph):
     for b in range(pw):
      R[i+a][j+b]=t[a][b];o[i+a][j+b]=m
    break
 return R

