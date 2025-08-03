def p(g):
    r=lambda g:[list(z)for z in zip(*g[::-1])]
    a=r(g);b=r(a)
    return [i+j for i,j in zip(g,a)]+[i+j for i,j in zip(r(b),b)]
