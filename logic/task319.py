def p(g):
    # compare border mini to shapes
    a=sum(g,[]);b=max(a,key=a.count);r=range;Y=len(g);X=len(g[0]);c=a.count;s={*a}-{b}
    for d in s:
        f=lambda t:[*zip(*([[b,d][q==d]for q in e]for e in t if d in e))]
        o=f(f(g));H=len(o)*2;W=len(o[0])*2
        for y in r(-H,Y):
            for x in r(-W,X):
                for q in s-{d}:
                    k=n=0
                    for i in r(H):
                        for j in r(W):
                            if Y>y+i>=0<=x+j<X:
                                v=g[y+i][x+j];k+=(o[i//2][j//2]==d)^(v==q);n+=v==q
                    if k<1 and n==c(q):return o
    return g
