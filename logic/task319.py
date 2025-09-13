def p(g):
    # compare border mini to shapes
    F=sum(g,[]);b=max(F,key=F.count);R=range;Y=len(g);X=len(g[0]);C=F.count
    for c in R(10):
        f=lambda t:[*zip(*([[b,c][q==c]for q in r]for r in t if c in r))]
        o=f(f(g))
        if c^b:
            H=len(o)*2;W=len(o and o[0])*2
            for y in R(-H,Y):
                for x in R(-W,X):
                    for q in R(10):
                        ok=cnt=0
                        for i in R(H):
                            for j in R(W):
                                if Y>y+i>=0<=x+j<X:
                                    v=g[y+i][x+j];ok+=(o[i//2][j//2]==c)^(v==q);cnt+=v==q
                        if ok<1 and cnt==C(q)>0 and q-c:return o
    return g