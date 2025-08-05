def p(g):
 m=len(g);n=len(g[0])
 a=next(i for i in range(1,m)if len(set(g[i]))==1)+1
 b=next(j for j in range(1,n)if len({r[j]for r in g})==1)+1
 B=[r[::b]for r in g[::a]];h=len(B);w=len(B[0]);d=(1,0,-1,0,1)
 for y in range(h):
  for x in range(w):
   if B[y][x]:
    q=[(y,x)];o={(y,x)};l=[B[y][x]]
    while q:
     y,x=q.pop()
     for k in range(4):
      Y=y+d[k];X=x+d[k+1]
      if 0<=Y<h and 0<=X<w and B[Y][X]and(Y,X)not in o:o.add((Y,X));q.append((Y,X));l.append(B[Y][X])
    if len(set(l))>1:break
  else:continue
  break
 t=next((B[y][x]for y in range(h)for x in range(w)if B[y][x]and(y,x)not in o),0)
 c=t if t in l else min(l,key=l.count)
 mn=min(y for y,_ in o);mx=min(x for _,x in o)
 ay,ax=min((y-mn,x-mx)for y,x in o if B[y][x]==c)
 P=[(B[y][x],y-mn-ay,x-mx-ax)for y,x in o]
 for y in range(h):
  for x in range(w):
   if B[y][x]==c and(y<1 or B[y-1][x]!=c)and(x<1 or B[y][x-1]!=c):
    for k,dy,dx in P:
     Y=y+dy;X=x+dx
     if 0<=Y<h and 0<=X<w:B[Y][X]=k
 return[[B[i//a][j//b]if i%a<a-1 and j%b<b-1 else g[i][j]for j in range(n)]for i in range(m)]

