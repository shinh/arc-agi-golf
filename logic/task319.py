def p(g):
    # compare border mini to shapes
    a=sum(g,[]);c=a.count;b=max(a,key=c);r=range;Y,X=len(g),len(g[0]);s={*a}-{b}
    for d in s:
        o=g
        for _ in 0,0:o=[*zip(*([[b,d][q==d]for q in e]for e in o if d in e))]
        H=len(o)*2;W=len(o[0])*2
        for y in r(-H,Y):
            for x in r(-W,X):
                for q in s-{d}:
                    k=n=0
                    for i in r(H):
                        for j in r(W):
                            if Y>y+i>=0<=x+j<X:
                                v=g[y+i][x+j];t=v==q;k+=(o[i//2][j//2]==d)^t;n+=t
                    if k+n==n==c(q):return o
    return g
