def p(g):
    # mirror shape across line of 2s
    o=[[3]*10 for _ in g]
    C=[(y,x)for y,r in enumerate(g)for x,v in enumerate(r)if v and v-2]
    T=[(y,x)for y,r in enumerate(g)for x,v in enumerate(r)if v==2]
    c=g[C[0][0]][C[0][1]]
    yc,xc=zip(*C);yt,xt=zip(*T)
    h=min(xt)>max(xc) or max(xt)<min(xc)
    if h:a=(min(xt)+max(xc),max(xt)+min(xc))[min(xt)<=max(xc)]
    else:a=(min(yt)+max(yc),max(yt)+min(yc))[min(yt)<=max(yc)]
    for y,x in C:y2,x2=[(a-y,x),(y,a-x)][h];o[y][x]=o[y2][x2]=c
    return o
