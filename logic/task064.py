def p(g):
    h=len(g);w=len(g[0]);a=sum(g,[]);b=max(a,key=a.count);o=[r[:]for r in g]
    for y in range(h):
        for x in range(w):
            c=g[y][x]
            if c-b:
                for Y,X in((1,0),(-1,0),(0,1),(0,-1)):
                    ny=y-Y;nx=x-X
                    if 0<=ny<h and 0<=nx<w and g[ny][nx]==c:continue
                    yy=y+Y;xx=x+X;n=0
                    while 0<=yy<h and 0<=xx<w and g[yy][xx]==b:yy+=Y;xx+=X;n+=1
                    if n and 0<=yy<h and 0<=xx<w and g[yy][xx]-b and g[yy][xx]-c:
                        for i in range(1,n+1):o[y+Y*i][x+X*i]=c
    return o
