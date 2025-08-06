def p(g):
    h=len(g);w=len(g[0])
    s={(i,j)for i in range(h)for j in range(w)if g[i][j]};m=set()
    while s:
        q=[s.pop()];o=set()
        while q:
            x,y=q.pop();o.add((x,y))
            for a in-1,0,1:
                for b in-1,0,1:
                    if a|b and(p:=(x+a,y+b))in s:s.remove(p);q+=p,
        if len(o)>len(m):m=o
    C={g[i][j]for i in range(h)for j in range(w)if g[i][j]and(i,j)not in m}
    rs,cs=zip(*m);a=min(rs);b=min(cs);H=max(rs)-a+1;W=max(cs)-b+1
    B=[(r-a,c-b,g[r][c])for r,c in m]
    I=[i for i,(_,_,v)in enumerate(B)if v in C]
    if not I:return g
    G=[*map(list,g)]
    for _ in range(2):
        for _ in range(4):
            a,b,k=(S:=[B[n]for n in I])[0];Q=[(i-a,j-b)for i in range(h)for j in range(w)if g[i][j]==k]
            for i,j in Q:
                if all(0<=i+r<h>0<=j+c<w and g[i+r][j+c]==k for r,c,k in S):
                    for r,c,k in B:
                        x,y=i+r,j+c
                        if 0<=x<h>0<=y<w:G[x][y]=k
            B=[(c,H-1-r,k)for r,c,k in B];H,W=W,H
        B=[(r,W-1-c,k)for r,c,k in B]
    return G
