def p(g):
    # flood-fill two-color objects and clone them
    h=len(g);w=len(g[0]);S=set();O=[r[:]for r in g]
    for i in range(h):
        for j in range(w):
            if g[i][j]and(i,j)not in S:
                q=[(i,j)];o=[]
                while q:
                    x,y=q.pop()
                    if(x,y)in S or g[x][y]<1:continue
                    S.add((x,y));o+=[(x,y,g[x][y])]
                    q+=[(x+a,y+b)for a in(-1,0,1)for b in(-1,0,1)if a|b and-1<x+a<h and-1<y+b<w]
                C={c for*_,c in o}
                if len(C)-2:continue
                I=min(p[0]for p in o);J=min(p[1]for p in o);o=[(a-I,b-J,c)for a,b,c in o]
                for c in C:
                    P=[(a,b)for a,b,t in o if t==c];pi=min(p[0]for p in P);pj=min(p[1]for p in P);R=[(a-pi,b-pj)for a,b in P]
                    for r in range(h):
                        for k in range(w):
                            if all(-1<r+di<h and-1<k+dj<w and g[r+di][k+dj]==c for di,dj in R):
                                for a,b,t in o:
                                    x=r+a-pi;y=k+b-pj
                                    if-1<x<h and-1<y<w:O[x][y]=t
    return O
