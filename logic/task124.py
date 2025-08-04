def p(g):
    h=len(g);w=len(g[0])
    flat=[v for r in g for v in r]
    bg=max(flat,key=flat.count)
    fg=[(i,j,g[i][j]) for i in range(h) for j in range(w) if g[i][j]!=bg]
    c=[]
    for dy in range(1,6):
        for dx in range(-10,10):
            m=o=0
            for i,j,v in fg:
                ni=i+dy;nj=j+dx
                if 0<=ni<h and 0<=nj<w:
                    o+=1
                    if g[ni][nj]==v:m+=1
            if o and m==o:c.append((m,dy,dx))
    if c:
        m=max(x[0] for x in c)
        dy,dx=max([x for x in c if x[0]==m],key=lambda x:x[1]*x[2])[1:]
    else:dy,dx=1,0
    out=[[bg]*w for _ in range(10)]
    for n in range(10):
        for i,j,v in fg:
            ni=i+dy*n;nj=j+dx*n
            if 0<=ni<10 and 0<=nj<w:out[ni][nj]=v
    return out
