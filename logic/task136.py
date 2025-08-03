def p(g):
    n=len(g)-1
    for y in range(n+1):
        for x in range(n+1):
            if g[y][x]==1:
                while y>=0 and x>=0:g[y][x]=1;y-=1;x-=1
                break
        else:continue
        break
    for y in range(n,-1,-1):
        for x in range(n,-1,-1):
            if g[y][x]==2:
                while y<n and x<n:y+=1;x+=1;g[y][x]=2
                return g
