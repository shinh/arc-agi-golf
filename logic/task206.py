def p(g):
    # copy 3x3 block to location of 5
    n=len(g[0]);h=sum(g,[]);y,x=map(min,zip(*[(i//n,i%n)for i,v in enumerate(h)if v%5]));i=h.index(5)+~n
    for j in 0,1,2:g[i//n+j][i%n:i%n+3]=g[y+j][x:x+3]
    return g
