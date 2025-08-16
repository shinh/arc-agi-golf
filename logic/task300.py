def p(g):
 # find most common color, crop its bbox
 f=sum(g,[]);v=max({*f}-{0},key=f.count);w=len(g[0])
 y,x=zip(*((i//w,i%w)for i,u in enumerate(f)if u==v))
 return[r[min(x):max(x)+1]for r in g[min(y):max(y)+1]]
