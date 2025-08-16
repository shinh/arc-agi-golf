def p(g):
    # extend from 2s
    o=[r[:]for r in g]
    for y in range(9):
        for x in range(9):
            if g[y][x]==0:continue
            s=[(y,x)];obj=[];my=mx=9;c=0;twos=[]
            while s:
                y1,x1=s.pop();v=g[y1][x1]
                if not v:continue
                obj+=[(y1,x1)];g[y1][x1]=0
                if v-2:c=v
                twos+=((y1,x1),)*(v==2)
                my=min(my,y1);mx=min(mx,x1)
                for dy,dx in((1,0),(-1,0),(0,1),(0,-1)):
                    ny,nx=y1+dy,x1+dx
                    if 0<=ny<9>nx>=0:s+=((ny,nx),)
            for dy,dx in((1-2*(a==my),1-2*(b==mx))for a,b in twos):
                for a,b in obj:
                    y2,x2=a,b
                    while 0<=y2<9>x2>=0:
                        o[y2][x2]=c;y2+=dy;x2+=dx
    return o

