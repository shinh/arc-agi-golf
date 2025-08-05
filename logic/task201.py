def p(g):
 h=len(g);w=len(g[0]);d={}
 for i,r in enumerate(g):
  for j,v in enumerate(r):d.setdefault(v,[]).append((i,j))
 for k,v in d.items():
  if len(v)==4:
   rs=[x for x,_ in v];cs=[y for _,y in v]
   if set(v)=={(min(rs),min(cs)),(min(rs),max(cs)),(max(rs),min(cs)),(max(rs),max(cs))}:
    c=k;pts=v;break
 r0,r1=min(x for x,_ in pts),max(x for x,_ in pts)
 c0,c1=min(y for _,y in pts),max(y for _,y in pts)
 sub=[row[c0:c1+1]for row in g[r0:r1+1]]
 bg=0
 cov=[row[:]for row in g]
 for i in range(r0,r1+1):
  for j in range(c0,c1+1):cov[i][j]=bg
 T=lambda M:list(map(list,zip(*M)))
 dmir=any(len(set(r))==1 for r in sub)
 if dmir:sub=T(sub);cov=T(cov)
 cells=[(v,i,j)for i,row in enumerate(cov)for j,v in enumerate(row)if v]
 if cells:
  mi=min(i for v,i,j in cells);mj=min(j for v,i,j in cells)
  cells=[(v,i-mi,j-mj)for v,i,j in cells]
 pal={v for row in sub for v in row if v}-{c}
 if len(pal)>1:
  a,b=sorted(pal)[0],sorted(pal)[-1]
  lm=lambda m,t:min(j for i,r in enumerate(m) for j,v in enumerate(r)if v==t)
  if (lm(sub,b)>lm(sub,a))!=(lm(cov,b)>lm(cov,a)):
   W=max(j for _,_,j in cells)+1
   cells=[(v,i,W-1-j)for v,i,j in cells]
 for v,i,j in cells:
  i+=1;j+=1
  if i<len(sub)and j<len(sub[0]):sub[i][j]=v
 if dmir:sub=T(sub)
 return sub
