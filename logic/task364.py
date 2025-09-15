def p(g):
    #show(g,"input")
    # recolor 3s by shape
    for o in range(80):
        for y,(r,pr,nr) in enumerate(zip(g,[[0]*99]+g,g[1:]+[[0]*99])):
            for x,(c,p,n,t,u) in enumerate(zip(r,[0]+r,r[1:]+[0],pr,nr)):
                if c==p==t==3:
                    g[y][x]=1+(n>0)+(u>0)
                elif c==n==t==3:
                    g[y][x]=1+(p>0)+(u>0)
                if c==3 and p==n==1:
                    g[y][x]=6
                elif p and c:
                    if 2 in (c,p):
                        g[y][x]=2
                    elif 6 in (c,p):
                        g[y][x]=6
                    elif 1 in (c,p) and o>8:
                        g[y][x]=1
        #if o%4==0:
        #    show(g,f"step{o:02}")
        g=[*map(list,zip(*g[::-1]))]
    #for t in range(80):
    #    g=[[[c,[max(c,p)+(c==p==1),p,c,c][(c==3)+(p==3)*2]][p>0 and c>0]for c,p in zip(r,(0,)+r)]for r in zip(*g[::-1])]
        #g=[[[c,max(c,p)+(c==p==1)][p>0 and c>0]for c,p in zip(r,(0,)+r)]for r in zip(*g[::-1])]
    #show(g,"output")
    return g
