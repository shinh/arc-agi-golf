def p(g):
    n=len(g);c=g[n//2][0]
    g=[r[:n//2]+r[n//2+1:]for i,r in enumerate(g)if i!=n//2]
    h=len(g)//2;t=[[c*(v>0)for v in r[:h]]for r in g[:h]]
    f=lambda a:[r[::-1]for r in a];b=t[::-1]
    return[x+y for x,y in zip(t,f(t))]+[x+y for x,y in zip(b,f(b))]
