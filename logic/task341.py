def p(g):
    # bridge shapes with 8
    for _ in 0,1:
        y1=99;y2=A=B=0
        for y,r in enumerate(g):
            s=''.join('10'[c<1]for c in r)
            x=s.find('10')+1
            X=s.find('1',x)
            if 0<x<X:
                A,B=x,X;y1=min(y1,y);y2=y
        for r in g[y1+1:y2]:
            r[A:B]=[8]*(B-A)
        g=[*map(list,zip(*g))]
    return g
