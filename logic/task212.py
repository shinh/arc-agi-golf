def p(g):
    r=[i for i,v in enumerate(g)if v.count(5)==10][0];o=[r[:]for r in g]
    for y,row in enumerate(g):
        for x,v in enumerate(row):
            if v==1:
                for k in range((0,y)[y>r],(y+1,10)[y>r]):o[k][x]=1
            elif v==2:
                for k in (range(y,r),range(r+1,y+1))[y>r]:o[k][x]=2
    return o
