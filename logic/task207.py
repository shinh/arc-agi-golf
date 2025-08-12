def p(g):
    q=[]
    for i in range(4):
        y=i//2*3
        x=i%2*3
        q+=[g[y][x:x+2],g[y+1][x:x+2]],
    return min(q,key=q.count)
