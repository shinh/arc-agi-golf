# extend lines from 2 toward 8, painting around the 8
def p(g):
    #show(g,"input")
    for _ in[0]*4:
        for y,r in enumerate(g):
            s=0
            for x,v in enumerate(r):
                if v==2:s=x+1
                if v==8!=r[0]and x>s>0:r[s-1:x+1]=[2]*(x+2-s);g[y-1][x-1]=g[y][x-1]=g[y+1][x-1]=g[y-1][x+1]=g[y][x+1]=g[y+1][x+1]=8;s=0
        #show(g,"o")
        g=[*map(list,zip(*g[::-1]))]
    return g
