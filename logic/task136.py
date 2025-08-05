def p(g):
    for y in range(10):
        for x in range(10):
            if g[y][x]==1:
                while y>=0 and x>=0:g[y][x]=1;y-=1;x-=1
                break
        else:continue
        break
    for y in range(9,-1,-1):
        for x in range(9,-1,-1):
            if g[y][x]==2:
                while y<9 and x<9:y+=1;x+=1;g[y][x]=2
                return g
