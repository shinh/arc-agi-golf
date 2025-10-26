def p(g):#rotate&scale
    c=[a for r,s in zip(g,g[1:]) for a,b,d,e in zip(r,r[1:],s,s[1:])if a==b==d==e>0][-1]
    A=sum({*sum(g,[])})-c
    for _ in[0]*96:g=[*zip(*g[(c in g[-1])-2::-1])]
    return[[A*(v==c)for v in R[::len(g)//3]]for R in g[::len(g)//3]]
