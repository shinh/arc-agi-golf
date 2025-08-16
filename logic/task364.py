def p(g):
    # recolor 3s by shape
    h=len(g);w=len(g[0]);v=set();D=(1,0,-1,0,0,1,0,-1)
    for y in range(h):
        for x in range(w):
            if g[y][x]-3 or (y,x)in v:continue
            q=[(y,x)];C=[]
            while q:
                y1,x1=q.pop();v.add((y1,x1));C+=[(y1,x1)]
                for i in 0,2,4,6:
                    ny=y1+D[i];nx=x1+D[i+1]
                    if 0<=ny<h and 0<=nx<w and g[ny][nx]==3 and (ny,nx)not in v:q+=[(ny,nx)]
            n=sum(sum(((p[0]+D[i],p[1]+D[i+1])in C)for i in (0,2,4,6))==1 for p in C)
            t=sum(((y-1,x)in C or (y+1,x)in C)and((y,x-1)in C or (y,x+1)in C)for y,x in C)
            c=2 if n>2 else [6,1][t<2]
            for y1,x1 in C:g[y1][x1]=c
    return g
