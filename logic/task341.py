def p(g):
    # bridge w/8
    for _ in'00':
        a=9;p=0
        for y,r in enumerate(g):
            f=''.join('01'[c>0]for c in r).find
            if 0<(x:=f('10')+1)<(t:=f('1',x)):
                A=x;B=t-x
                a=min(a,p:=y)
        for r in g[a+1:p]:r[A:A+B]=[8]*B
        g=[*map(list,zip(*g))]
    return g
