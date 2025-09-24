def p(g):# draw inner color rectangle just inside 5s
    y,x=zip(*((y,x)for y,r in enumerate(g)for x,c in enumerate(r)if c==5));t=min(y)+1;b=max(y);l=min(x)+1;r=max(x);h=g[t:b]
    c=max(max(w[l:r])for w in h)
    h[0][l:r]=h[-1][l:r]=[c]*(r-l)
    for w in h:w[l]=w[r-1]=c
    return g
