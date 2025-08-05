def p(g):
    grays=[]
    colors=[0]
    seps=[-1]
    for x in range(len(g[0])):
        l=[g[y][x]for y in range(3)]
        if not any(l):
            colors+=[0]
            seps+=[x]
        for y in range(3):
            if g[y][x]==5:
                grays+=[y]
            elif g[y][x]>0:
                colors[-1]=g[y][x]
    seps+=[len(g[0])]
    grays+=[0]

    #show(g, "c")
    #print(grays)

    out=[[]for _ in g]
    prev_offset=0
    for i in range(len(colors)-(colors[-1]==0)):
        #print(i)
        offset=[0,grays[i*2-1]][i>0]

        for y in range(3):
            fy=y+offset-prev_offset
            out[y]+=[0]*(seps[i+1]-seps[i]-1)if fy<0 or fy>=3 else[[c,colors[i]][c==5]for c in g[fy][seps[i]+1:seps[i+1]]]
        prev_offset+=grays[i*2]-offset

    #show(out, "out")
    return out
