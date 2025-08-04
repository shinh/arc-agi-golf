def p(g):
    a=b=0
    for i,r in enumerate(g):
        for j,v in enumerate(r):
            if v==2:a,b=i,j
    d=1-(a<2 and g[a+1][b]==3);e=1-(b<2 and g[a][b+1]==3)
    r=5*(1-d);c=5*(1-e)
    o=[[0]*9 for _ in range(9)]
    for x,y in((r,c),(r+(4 if d else -4),c+(4 if e else -4))):
        for i in range(x,x+4):o[i][y:y+4]=[3]*4
    return o
