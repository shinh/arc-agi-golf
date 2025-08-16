def p(g):
    # tile g where color repeats; zeros set grid size
    f=sum(g,[]);z=f.count(0);r=range(z*3)
    return [[g[y%3][x%3]*(z*(y//3)+x//3<9-z)for x in r]for y in r]
