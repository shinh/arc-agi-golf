def p(g):
    # join23
    a=sum(g,[]);w=len(g[0]);i=a.index(2);j=a.index(3)
    while (i:=i+((j%w>i%w)-(j%w<i%w) or w*((j>i)-(j<i))))-j:g[i//w][i%w]=8
    return g
