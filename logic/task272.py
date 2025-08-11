def p(g):
    for r,pr,nr in zip(g,[[0]*99]+g,g[1:]+[[0]*99]):
        for i in range(len(r)):
            if r[i]and[*r[1:],0][i]+[0,*r][i]+pr[i]+nr[i]<1:
                r[i]=1
    return g
