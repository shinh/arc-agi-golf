def p(g):
    # extend from 2s
    o=[r[:]for r in g]
    for y in range(9):
        for x in range(9):
            if g[y][x]:
                s=[(y,x)];obj=[];tw=[];my=mx=9;c=0
                for Y,X in s:
                    if v:=g[Y][X]:
                        obj+=[(Y,X)];g[Y][X]=0;c=c or v-2 and v;tw+=[(Y,X)]*(v==2);my=min(my,Y);mx=min(mx,X)
                        for a,b in((1,0),(-1,0),(0,1),(0,-1)):
                            ny,nx=Y+a,X+b
                            if 9>ny>=0<=nx<9:s+=[(ny,nx)]
                for a,b in tw:
                    dy=1-2*(a==my);dx=1-2*(b==mx)
                    for a,b in obj:
                        Y,X=a,b
                        while 9>Y>=0<=X<9:o[Y][X]=c;Y+=dy;X+=dx
    return o

