def p(g):
    h=len(g);w=len(g[0])
    seen=set()
    for i in range(h):
        for j in range(w):
            if g[i][j]==0 or(i,j)in seen:continue
            c=g[i][j];q=[(i,j)];obj=set()
            while q:
                x,y=q.pop()
                if(x,y)in seen or g[x][y]!=c:continue
                seen.add((x,y));obj.add((x,y))
                for a in(-1,0,1):
                    for b in(-1,0,1):
                        if a or b:
                            u,v=x+a,y+b
                            if 0<=u<h and 0<=v<w:q.append((u,v))
            mi=min(x for x,_ in obj);mj=min(y for _,y in obj)
            ma=max(x for x,_ in obj);mb=max(y for _,y in obj)
            w0=mb-mj+1
            norm={(x-mi,y-mj)for x,y in obj}
            if all((x,w0-1-y)in norm for x,y in norm):
                return[ r[mj:mb+1] for r in g[mi:ma+1] ]
    return g
