def p(g):
    h=len(g);w=len(g[0])
    f=sum(g,[])
    p=min(f,key=f.count)
    u=[]
    for y in range(h):
        for x in range(w):
            m=[]
            for dy in range(-4,5):
                for dx in range(-4,5):
                    if 0<=y+dy<h and 0<=x+dx<w and p!=g[y+dy][x+dx]:
                        m+=g[y+dy][x+dx],
            m=max(m,key=m.count)
            if p==g[y][x]:
                u+=m,
    return[[max(u,key=u.count)]]
