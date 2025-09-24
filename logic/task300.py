def p(g):
 # find most common color, crop its bbox
 f=sum(g,[]);v=max({*f}-{0},key=f.count);y,x=zip(*(divmod(i,len(g[0]))for i,u in enumerate(f)if u==v));return[r[min(x):max(x)+1]for r in g[y[0]:y[-1]+1]]
