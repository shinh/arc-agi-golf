# extend lines from 2 toward 8, painting around the 8
def p(g):
    #show(g,"input")
    for _ in[0]*4:
        for y,r in enumerate(g):
            s=0
            for x,v in enumerate(r):
                if v==2:s=x+1
                if v==8 and r[0]-8 and x>s>0:
                    r[s-1:x+1]=[2]*(x+2-s)
                    for Y in y-1,y,y+1:g[Y][x-1:x+2:2]=8,8
                    s=0
        #show(g,"o")
        g=[[*r]for r in zip(*g[::-1])]
    return g
