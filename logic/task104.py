def p(g):
    a=1-g[0][1]//3;b=1-g[1][0]//3
    c=5*b+a*(4-8*b);s=[3]*4;o=[[0]*9 for _ in[0]*9]
    for x,y in((a,c),(a+4,c+4-8*(a^b))):
        for i in range(4):o[x+i][y:y+4]=s
    return o
