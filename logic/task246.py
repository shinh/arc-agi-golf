def p(g):# join23
    w=len(g[0]);i,j=map(sum(g,[]).index,(2,3))
    while(i:=i+((j%w>i%w)-(j%w<i%w)or w*(1,-1)[i>j]))-j:g[i//w][i%w]=8
    return g
