def p(g):
    # flood-fill two-color objects and clone them
    h=len(g);w=len(g[0]);O=[*map(list,g)]
    for i in range(h):
        for j in range(w):
            if O[i][j]<1:continue
            q=[(i,j)];o=[]
            while q:
                x,y=q.pop()
                if O[x][y]<1:continue
                o+=[(x,y,O[x][y])];O[x][y]=0
                q+=[(x+a,y+b)for a in(-1,0,1)for b in(-1,0,1)if a|b and-1<x+a<h and-1<y+b<w]
            C={c for*_,c in o}
            if len(C)-2:continue
            I,J,_=map(min,zip(*o));o=[(a-I,b-J,c)for a,b,c in o]
            for c in C:
                R=[(a,b)for a,b,t in o if t==c];pi,pj=map(min,zip(*R));R=[(a-pi,b-pj)for a,b in R]
                for r in range(h):
                    for k in range(w):
                        if all(-1<r+di<h and-1<k+dj<w and g[r+di][k+dj]==c for di,dj in R):
                            for a,b,t in o:
                                x=r+a-pi;y=k+b-pj
                                if-1<x<h and-1<y<w:O[x][y]=t
    return O
