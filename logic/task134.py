def p(g):#crop
    c=[a for r,s in zip(g,g[1:]) for a,b,d,e in zip(r,r[1:],s,s[1:])if a==b==d==e>0][-1];A=sum({*sum(g,[])})-c
    g=[r for r in g if c in r];g=[*zip(*g)];g=[r for r in g if c in r];g=[*zip(*g)];s=len(g)//3
    return[[A*(v==c)for v in R[::s]]for R in g[::s]]
