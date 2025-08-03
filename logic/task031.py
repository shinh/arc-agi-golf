def p(g):
    # gは二次元配列で、0-9の値が入っています。黒くない矩形 crop
    u=len(g);l=len(g[0]);d=r=0
    for y,row in enumerate(g):
        for x,v in enumerate(row):
            if v:u=min(u,y);l=min(l,x);d=max(d,y);r=max(r,x)
    return [row[l:r+1] for row in g[u:d+1]]
