def p(g):
    t=[(y,x)for y,r in enumerate(g)for x,v in enumerate(r)if v];y,x=zip(*t);a,b=min(y),max(y)+1;c,d=min(x),max(x)+1;return [r[c:d][::-1]for r in g[a:b]]
