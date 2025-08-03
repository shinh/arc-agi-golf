def p(g):
    B=[(y,x,[g[y+i][x+j]for i in range(3)for j in range(3)if g[y+i][x+j]not in(0,5)])for y in range(0,9,4)for x in range(0,9,4)]
    m=max(len(t)for _,_,t in B)
    for y,x,t in B:
        k=t[0]if len(t)==m and m else 0
        for i in range(3):g[y+i][x:x+3]=[k]*3
    return g
