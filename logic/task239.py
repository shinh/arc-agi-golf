def p(g):
    # histogram
    t=sum(g,[])
    s=sorted({*t}-{0},key=lambda c:(-t.count(c),c))
    return [[(t.count(c)>i)*c for c in s]for i in range(t.count(s[0]))]
