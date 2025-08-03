def p(g):
    w=len(g[0]);x=[i for i in range(w) if all(r[i]==8 for r in g)];y=[i for i,r in enumerate(g) if all(c==8 for c in r)]
    a,b=x;c,d=y
    for i,r in enumerate(g):
        if i<c:r[a+1:b]=[2]*(b-a-1)
        elif i>d:r[a+1:b]=[1]*(b-a-1)
        elif c<i<d:
            r[:a]=[4]*a;r[a+1:b]=[6]*(b-a-1);r[b+1:]=[3]*(w-b-1)
    return g
