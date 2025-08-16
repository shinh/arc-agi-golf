def p(g):
    #3x3 union around 5s
    a=-1,0,1;e=enumerate;return[[max(g[y+i][x+j]for y,r in e(g)for x,v in e(r)if v==5)for j in a]for i in a]
