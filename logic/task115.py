def p(g):
    h=len(g);w=len(g[0])
    r=g[h//2];c=[g[i][w//2] for i in range(h)]
    sr=sum(r[i]!=r[i-1] for i in range(1,w))
    sc=sum(c[i]!=c[i-1] for i in range(1,h))
    def f(a):
        b=[]
        for v in a:
            if not b or b[-1]!=v:b.append(v)
        return b
    if sr>sc:return [f(r)]
    return [[v] for v in f(c)]
