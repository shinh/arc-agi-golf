def p(g):
 h=len(g);w=len(g[0])
 c={}
 for r in g:
  for v in r:c[v]=c.get(v,0)+1
 bg=max(c,key=c.get);c.pop(bg);M=max(c,key=c.get)
 vis=set();comps=[]
 for i in range(h):
  for j in range(w):
   if g[i][j]!=bg and (i,j)not in vis:
    q=[(i,j)];vis.add((i,j));comp=[]
    while q:
     x,y=q.pop();comp.append((x,y))
     for dx,dy in((1,0),(-1,0),(0,1),(0,-1)):
      nx,ny=x+dx,y+dy
      if 0<=nx<h and 0<=ny<w and g[nx][ny]!=bg and (nx,ny)not in vis:
       vis.add((nx,ny));q.append((nx,ny))
    comps.append(comp)
 big=max(comps,key=len)
 T=min(i for i,j in big);B=max(i for i,j in big)
 L=min(j for i,j in big);R=max(j for i,j in big)
 orig=[row[L:R+1] for row in g[T:B+1]]
 res=[[M]*len(orig[0]) for _ in orig]
 objs=[]
 for comp in comps:
  if comp==big:continue
  xs=[i for i,j in comp];ys=[j for i,j in comp]
  t,b=min(xs),max(xs);l,r=min(ys),max(ys)
  if (b-t+1)*(r-l+1)!=len(comp):continue
  patch=[row[l:r+1] for row in g[t:b+1]]
  cols={v for row in patch for v in row}
  if len(cols)==2 and M in cols:objs.append(patch)
 def trans(p):
  r=[p]
  for _ in range(3):
   p=[list(z) for z in zip(*p[::-1])];r.append(p)
  return r+[[row[::-1] for row in q] for q in r]
 H0=len(orig);W0=len(orig[0])
 for pch in objs:
  for t in trans(pch):
   ph=len(t);pw=len(t[0]);slots=[]
   for i in range(H0-ph+1):
    for j in range(W0-pw+1):
     if all((t[a][b]==M)==(orig[i+a][j+b]==0) for a in range(ph) for b in range(pw)):
      slots.append((i,j))
   if slots:
    i,j=slots[-1]
    if i==0 or j==0 or i+ph==H0 or j+pw==W0:i,j=slots[0]
    for a in range(ph):
     for b in range(pw):
      res[i+a][j+b]=t[a][b];orig[i+a][j+b]=M
    break
 return res
