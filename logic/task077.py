# 200
def p(g):
    for i in range(20):
        for y,r in enumerate(g):
            for x,(c,*t)in enumerate(zip(r,*g)):
                if(x>0 and r[x-1]in(2,4))+(y>0 and t[y-1]in(2,4))+((r+[0])[x+1]in(2,4))+((t+[0])[y+1]in(2,4))>1 and c!=2:
                    g[y][x]=4
    return g
