def p(g):
    # find shapes
    a,b=sorted({c for r in g for c in r if c})
    ps=lambda v:[(i,j)for i,r in enumerate(g)for j,x in enumerate(r)if x==v]
    n=lambda s:{(i-min(i for i,_ in s),j-min(j for _,j in s))for i,j in s}
    s1,s2=map(n,(ps(a),ps(b)))
    R=range(3);A={(i,j)for i in R for j in R}
    for y in R:
        for x in R:
            t={(i+y,j+x)for i,j in s1 if i+y<3>j+x}
            if n(A-t)==s2:
                return [[a*((i,j)in t)or b for j in R]for i in R]
