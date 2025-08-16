def p(g):
    # link every 8 to the side wall then duplicate its row
    W=len(g[0]);s=sum(g,[]);P=[divmod(i,W)for i,v in enumerate(s)if v==2];E=[divmod(i,W)for i,v in enumerate(s)if v==8]
    lc,st=min((x,y)for y,x in P);rc,ot=max((x,-y)for y,x in P);ot=-ot
    if all(g[y][lc]-2 and x-lc for y,x in E):lc,st,ot=rc,ot,st
    for y,x in E:
        a,b=sorted((lc,x));g[y][a+1:b]=[8]*(b-a-1);g[y][x]=4;r=y+ot-st
        if 0<=r<len(g):g[r]=[8]*W
    for y,x in P:g[y][x]=2
    return g
