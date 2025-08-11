# We can assume g has only 0 and 2. Isolated pixels must become to 1.
def p(g):
    return [[r[i]-(r[i]and[*r[1:],0][i]+[0,*r][i]+pr[i]+nr[i]<1)for i in range(len(r))]for r,pr,nr in zip(g,[[0]*9]+g,g[1:]+[[0]*9])]
