def p(g):
    h=len(g);w=len(g[0])
    z=[(y,x)for y in range(h)for x in range(w)if g[y][x]]
    if not z:return g
    if any(y==0 for y,_ in z):dy,dx=1,0
    elif any(y==h-1 for y,_ in z):dy,dx=-1,0
    elif any(x==0 for _,x in z):dy,dx=0,1
    else:dy,dx=0,-1
    r=[[0]*w for _ in range(h)];v=set()
    for s in z:
        if s in v:continue
        c=g[s[0]][s[1]];q=[s];v.add(s);pts=[];ys=[s[0]];xs=[s[1]]
        while q:
            y,x=q.pop();pts.append((y,x))
            for a,b in((1,0),(-1,0),(0,1),(0,-1)):
                u,vv=y+a,x+b
                if 0<=u<h and 0<=vv<w and g[u][vv]==c and (u,vv)not in v:
                    v.add((u,vv));q.append((u,vv));ys.append(u);xs.append(vv)
        sh=(max(ys)-min(ys)+1)*dy;sw=(max(xs)-min(xs)+1)*dx
        for y,x in pts:
            u,vv=y+sh,x+sw
            if 0<=u<h and 0<=vv<w:r[u][vv]=c
    return r
