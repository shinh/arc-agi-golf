def p(g):
 d={}
 for r in g:
  for v in r:
   if v:d[v]=d.get(v,0)+1
 a=max(d,key=d.get);b=min(d,key=d.get)
 H=len(g);W=len(g[0]);m=0
 for y in range(H):
  for x in range(W):
   for h in range(2,H-y+1):
    for w in range(2,W-x+1):
     if h*w>m and all(g[y+i][x+j]==a for i in range(h) for j in range(w) if i in(0,h-1) or j in(0,w-1)):
      m=h*w;R=y,x,h,w
 y,x,h,w=R
 return[[[v,b][v==a]for v in r[x:x+w]]for r in g[y:y+h]]
