# Far from best (123)
def p(g):
    def get(y,x):
        if y<0 or y>11 or x<0 or x>11:
            return 0
        return g[y][x]

    for dy,dx in ((1,1),(1,-1),(-1,1),(-1,-1)):
        ng=[[*r]for r in g]
        found_r=0
        for oy in range(12):
            for x in range(12):
                y=oy
                if g[y][x]&get(y-dy,x-dx)==8:
                    y+=dy
                    x+=dx
                    while 0<=x<12and 0<=y<12:
                        if g[y][x]==2:
                            found_r=1
                            y-=dy
                            x-=dx
                            if get(y+dy-1,x+dx)&get(y+dy+1,x+dx)==2:
                                dx=-dx
                            else:
                                dy=-dy
                            #print('found',y,x,dy,dx)
                            #show(ng,'kkk')
                            continue
                        if g[y][x]!=0:
                            break
                        ng[y][x]=3
                        y+=dy
                        x+=dx
        g=[g,ng][found_r]
    return g