def p(g):
    # compare border mini to shapes
    a=sum(g,[]);c=a.count;b=max(a,key=c);r=range;Y,X=len(g),len(g[0]);s={*a}-{b}
    for d in s:
        o=g
        for _ in 0,0:o=[*zip(*([[b,d][q==d]for q in e]for e in o if d in e))]
        H=len(o)*2;W=len(o[0])*2
        if any(c(q)==sum(0<=y+i<Y and 0<=x+j<X and o[i//2][j//2]==d and g[y+i][x+j]==q for i in r(H) for j in r(W))==sum(0<=y+i<Y and 0<=x+j<X and o[i//2][j//2]==d for i in r(H) for j in r(W))for y in r(-H,Y)for x in r(-W,X)for q in s-{d}):return o
    return g
