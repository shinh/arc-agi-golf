def p(g):
 R=range
 h,w=len(g),len(g[0])
 v=set()
 # loops
 def d(i,j):
  if(i,j)in v or not(-1<i<h and -1<j<w)or g[i][j]-1:return set()
  v.add((i,j))
  return {(i,j)}|d(i+1,j)|d(i-1,j)|d(i,j+1)|d(i,j-1)
 for i in R(h):
  for j in R(w):
   if g[i][j]==1 and(c:=d(i,j)):
    a,b=zip(*c)
    t,m,l,n=min(a),max(a),min(b),max(b)
    if len(c)==2*(m-t+n-l)and(m-t)*(n-l)and any(g[x][y]<1for x in R(t+1,m)for y in R(l+1,n)):
     for x,y in c:g[x][y]=3
 return g
