def p(g):
    P=set(sum(g,[]));H=len(g);W=len(g[0])
    def pal(b):return{v for r in b for v in r}
    def part(b):return{frozenset((i,j)for i,r in enumerate(b) for j,v in enumerate(r)if v==c)for c in pal(b)}
    def sig(b):return frozenset(part(b))
    def vs(n):
        h=H//n;o=H%n>0
        return[[r[:W]for r in g[h*i+i*o:h*i+i*o+h]]for i in range(n)]
    def hs(n):
        w=W//n;o=W%n>0
        return[[r[w*i+i*o:w*i+i*o+w]for r in g]for i in range(n)]
    def sc(s):
        t=[pal(b)for b in s]
        x=any(all(c in p for p in t)for c in P)
        y=len({(len(b),len(b[0])if b else 0)for b in s})==1
        z=len({sig(b)for b in s})==2
        w=len({tuple(map(tuple,b))for b in s})==len(s)
        return(x+y+z+w)*100+len(s)
    C=[vs(n)for n in range(3,H//2+1)]+[hs(n)for n in range(3,W//2+1)]
    S=max(C,key=sc)
    sigs=[sig(b)for b in S];mc=max(sigs,key=sigs.count)
    for b in S:
        if sig(b)!=mc:return b
    return S[0]

