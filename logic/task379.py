# extend lines from 2 toward 8, painting around the 8
def p(g):
    #show(g,"input")
    for o in range(4):
        for y,r in enumerate(g):
            s=99
            if 8 in r and r[0]!=8:
                for x in range(len(r)):
                    if r[x]==2:s=x
                    if r[x]==8 and x-s>1:
                        #r[s:x+1]=[2]*(x+1-s)
                        r[s:x+1]=[2]*(x+1-s)
                        g[y][x-1]=g[y][x+1]=g[y-1][x-1]=g[y-1][x+1]=g[y+1][x-1]=g[y+1][x+1]=8
                        s=99

        #show(g,"o")
        g=[*map(list,zip(*g[::-1]))]
    return g