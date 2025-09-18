# flood-fill largest island and stamp rotated/flip copies wherever its special colors appear
def p(g):
    h=len(g);w=len(g[0])
    s={(i,j)for i in range(h)for j in range(w)if g[i][j]};t=s.copy();m=[]
    while s:
        q=[s.pop()]
        for x,y in q:
            for a in-1,0,1:
                for b in-1,0,1:
                    if a|b and(p:=(x+a,y+b))in s:s.remove(p);q+=p,
        m=max(m,q,key=len)
    C={g[i][j]for i,j in t if(i,j)not in m}
    rs,cs=zip(*m);a=min(rs);b=min(cs)
    B=[(r-a,c-b,g[r][c])for r,c in m]
    G=[r[:]for r in g]
    for _ in'01':
        for _ in'0000':
            if not(S:=[b for b in B if b[2]in C]):return g
            a,b,k=S[0]
            for i,j in[(i-a,j-b)for i in range(h)for j in range(w)if g[i][j]==k]:
                if all(h>i+r>-1<j+c<w and g[i+r][j+c]==k for r,c,k in S):
                    for r,c,k in B:
                        if h>i+r>-1<j+c<w:G[i+r][j+c]=k
            B=[(c,-r,k)for r,c,k in B]
        B=[(r,-c,k)for r,c,k in B]
    return G
