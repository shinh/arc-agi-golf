# replicate majority pattern

def p(g):
 r=[*map(list,g)];h=len(g);w=len(g[0]);R=range(-1,2)
 for i in range(h):
  for j in range(w):
   if g[i][j]<1:continue
   st=[(i,j)];c=[]
   while st:
    x,y=st.pop()
    if g[x][y]<1:continue
    g[x][y]=0;c+=((x,y,r[x][y]),)
    st+=[(x+a,y+b)for a in R for b in R if(a|b)and-1<x+a<h and-1<y+b<w]
   m=max(t:=[V for x,y,V in c],key=t.count)
   e=[(x,y)for x,y,V in c if V==m];xs,ys=zip(*e)
   H=max(xs)-(mi:=min(xs))+1;W=max(ys)-(mj:=min(ys))+1;P=[(x-mi,y-mj)for x,y in e]
   for x,y,V in c:
    if V-m:
     oi=mi+(di:=(x-mi)//H)*H;oj=mj+(dj:=(y-mj)//W)*W
     for p,q in P:
      if-1<(u:=oi+(H-1-p if di&1 else p))<h and-1<(v:=oj+(W-1-q if dj&1 else q))<w:r[u][v]=V
 return r
