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
    g[x][y]=0;c+=[(x,y,r[x][y])]
    st+=[(u,v)for a in R for b in R if(a|b)and-1<(u:=x+a)<h and-1<(v:=y+b)<w]
   m=max(cols:=[v for x,y,v in c],key=cols.count)
   maj=[(x,y)for x,y,v in c if v==m];xs,ys=zip(*maj)
   mi,mj=min(xs),min(ys);H=max(xs)-mi+1;W=max(ys)-mj+1;P=[(x-mi,y-mj)for x,y in maj]
   for x,y,v in c:
    if v!=m:
     di,dj=(x-mi)//H,(y-mj)//W;oi,oj=mi+di*H,mj+dj*W
     for p,q in P:
      if di%2:p=H-1-p
      if dj%2:q=W-1-q
      if -1<oi+p<h and-1<oj+q<w:r[oi+p][oj+q]=v
 return r
