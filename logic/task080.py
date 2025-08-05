def p(g):
 m=len(g);n=len(g[0]);R=range
 a=next(i+1 for i in R(1,m)if len(set(g[i]))==1)
 b=next(j+1 for j in R(1,n)if len({r[j]for r in g})==1)
 B=[r[::b]for r in g[::a]];h=len(B);w=len(B[0]);d=1,0,-1,0,1
 for y in R(h):
  for x in R(w):
   if B[y][x]:
    q=[(y,x)];o={(y,x)};l=[B[y][x]]
    while q:
     y,x=q.pop()
     for k in R(4):
      Y,X=y+d[k],x+d[k+1]
      if 0<=Y<h and 0<=X<w and B[Y][X]and(Y,X)not in o:o.add((Y,X));q+=[(Y,X)];l+=B[Y][X],
    if len({*l})>1:break
  else:continue
  break
 c=next((B[y][x]for y in R(h)for x in R(w)if B[y][x]in l and(y,x)not in o),min(l,key=l.count))
 mn=min(y for y,_ in o);mx=min(x for _,x in o)
 ay,ax=min((y-mn,x-mx)for y,x in o if B[y][x]==c)
 P=[(B[y][x],y-mn-ay,x-mx-ax)for y,x in o]
 for y in R(h):
  for x in R(w):
   if B[y][x]==c and(y<1 or B[y-1][x]!=c)and(x<1 or B[y][x-1]!=c):
    for k,dy,dx in P:
     Y,X=y+dy,x+dx
     if 0<=Y<h and 0<=X<w:B[Y][X]=k
 return[[B[i//a][j//b]if(i+1)%a and(j+1)%b else g[i][j]for j in R(n)]for i in R(m)]

