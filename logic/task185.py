# 158
def p(g):
    c=max(g[0])
    for _ in 0,1:g=[r for r in zip(*g)if{*r}-{0,c}]
    return[[i*(i==j==k==l!=c)for i,j,k,l in zip(r,r[1:],nr,nr[1:])]for r,nr in zip(g,g[1:])]