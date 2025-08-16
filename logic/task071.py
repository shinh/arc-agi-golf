def p(g):
 h=16;d={}
 # collect colored positions
 [d.setdefault(v,set()).add((y,x))for y,r in enumerate(g)for x,v in enumerate(r)if v]
 for c,s in d.items():
  ys,xs=zip(*s);A=(max(ys)-min(ys)+1)*(max(xs)-min(xs)+1)
  if len(s)==A:rc=s
  else:sh=s;S=c
 ys,xs=zip(*sh);a=max(ys)+min(ys);b=max(xs)+min(xs)
 best=set();sc=-1;R=range(-h,h+1)
 # mirror shape and slide to overlap
 for P in({(i,b-j)for i,j in sh},{(a-i,j)for i,j in sh}):
  for dj in R:
   for di in R:
    s={(i+di,j+dj)for i,j in P}
    t=len(s&sh)
    if t>sc and all(i<0 or i>=h or j<0 or j>=h or g[i][j] for i,j in s):sc=t;best=s
 for i,j in rc:g[i][j]=0
 for i,j in best:g[i][j]=S
 return g
