def p(g):
    h=len(g);w=len(g[0]);v=set();D=((1,0),(-1,0),(0,1),(0,-1))
    for y in range(h):
        for x in range(w):
            if g[y][x]-3 or (y,x)in v:continue
            q=[(y,x)];v.add((y,x));C=set()
            while q:
                y1,x1=q.pop();C.add((y1,x1))
                for dy,dx in D:
                    ny,nx=y1+dy,x1+dx
                    if 0<=ny<h and 0<=nx<w and g[ny][nx]==3 and (ny,nx)not in v:
                        v.add((ny,nx));q.append((ny,nx))
            E=[p for p in C if sum(((p[0]+dy,p[1]+dx)in C)for dy,dx in D)==1]
            if len(E)>2:c=2
            else:
                y,x=E[0];py,px=y,x
                for dy,dx in D:
                    ny,nx=y+dy,x+dx
                    if (ny,nx)in C:break
                y,x,ay,ax=ny,nx,dy,dx;t=0
                while (y,x)!=E[1]:
                    for dy,dx in D:
                        ny,nx=y+dy,x+dx
                        if (ny,nx)in C and (ny,nx)!=(py,px):
                            t+=(dy!=ay or dx!=ax);py,px,y,x=y,x,ny,nx;ay,ax=dy,dx;break
                c=1 if t<2 else 6
            for y1,x1 in C:g[y1][x1]=c
    return g
