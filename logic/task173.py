def p(g):
    h=len(g);w=len(g[0])
    seen=set();objs=[]
    for i in range(h):
        for j in range(w):
            if g[i][j] and (i,j)not in seen:
                q=[(i,j)];o=[]
                while q:
                    x,y=q.pop()
                    if(x,y)in seen or g[x][y]==0:continue
                    seen.add((x,y));o.append((x,y,g[x][y]))
                    for a in(-1,0,1):
                        for b in(-1,0,1):
                            if a or b:
                                u,v=x+a,y+b
                                if 0<=u<h and 0<=v<w:q.append((u,v))
                objs.append(o)
    out=[r[:]for r in g]
    for o in objs:
        cs={c for _,_,c in o}
        if len(cs)!=2:continue
        oi=min(i for i,_,_ in o);oj=min(j for _,j,_ in o)
        o=[(i-oi,j-oj,c)for i,j,c in o]
        for c in cs:
            pts=[(i,j)for i,j,t in o if t==c]
            pi=min(i for i,_ in pts);pj=min(j for _,j in pts)
            rel=[(i-pi,j-pj)for i,j in pts]
            ph=max(i for i,_ in rel)+1;pw=max(j for _,j in rel)+1
            for r in range(h-ph+1):
                for k in range(w-pw+1):
                    if all(g[r+di][k+dj]==c for di,dj in rel):
                        for a,b,t in o:
                            x=r+a-pi;y=k+b-pj
                            if 0<=x<h and 0<=y<w:out[x][y]=t
    return out
