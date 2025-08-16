def p(g):
 d={}
 # collect colored positions
 [d.setdefault(v,set()).add(divmod(i,16))for i,v in enumerate(sum(g,[]))if v]
 (c1,s1),(c2,s2)=d.items()
 ys,xs=zip(*s1)
 rc,sh,S=(s1,s2,c2)if len(s1)==(max(ys)-min(ys)+1)*(max(xs)-min(xs)+1)else(s2,s1,c1)
 _,xs=zip(*sh);b=max(xs)+min(xs)
 best=set();sc=0
 # mirror shape and slide to overlap
 for dj in range(-2,2):
  s={(i,b-j+dj)for i,j in sh};t=len(s&sh)
  if t>sc and all(j<0 or j>15 or g[i][j] for i,j in s):sc=t;best=s
 for i,j in rc:g[i][j]=0
 for i,j in best:g[i][j]=S
 return g

