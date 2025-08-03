def p(g):
    h=len(g);w=len(g[0]);v=set();cm=[]
    for y in range(h):
        for x in range(w):
            if g[y][x]and(y,x)not in v:
                q=[(y,x)];c=[]
                while q:
                    y1,x1=q.pop()
                    if not(0<=y1<h and 0<=x1<w)or g[y1][x1]==0 or(y1,x1)in v:continue
                    v.add((y1,x1));c.append((y1,x1,g[y1][x1]))
                    q+=((y1+1,x1),(y1-1,x1),(y1,x1+1),(y1,x1-1))
                cm.append(c)
    t=[c for c in cm if len(c)>1]
    mk=[c[0] for c in cm if len(c)==1]
    M={(y,x):c for y,x,c in mk}
    u=set();o=[[0]*w for _ in range(h)]
    for a in t:
        cnt={}
        for _,_,c in a:cnt[c]=cnt.get(c,0)+1
        ay,ax=[(y,x)for y,x,c in a if c==1][0]
        r=[(y-ay,x-ax,c)for y,x,c in a]
        uq=[c for c in cnt if cnt[c]==1 and c!=1]
        for y1,x1,c1 in mk:
            if c1-1 or(y1,x1)in u:continue
            for R in range(4):
                for F in(0,1):
                    g2=True;off={}
                    for dy,dx,c in r:
                        dy2,dx2=dy,dx
                        if F:dy2=-dy2
                        for _ in range(R):dy2,dx2=-dx2,dy2
                        if c in uq:
                            yy,xx=y1+dy2,x1+dx2
                            if M.get((yy,xx))!=c or (yy,xx) in u:g2=False;break
                            off[c]=(dy2,dx2)
                    if g2:
                        for dy,dx,c in r:
                            if F:dy=-dy
                            for _ in range(R):dy,dx=-dx,dy
                            o[y1+dy][x1+dx]=c
                        u.add((y1,x1))
                        for dy,dx in off.values():u.add((y1+dy,x1+dx))
                        break
                if g2:break
            if g2:break
    return o
