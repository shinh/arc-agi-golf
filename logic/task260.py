def p(g):
    # draw diagonal line when 5 has empty cross arms
    for y in range(9):
        for x in range(9):
            if (c:=g[y][x])==5:
                for d in 1,-1:
                    a=y-d; b=x+d
                    if g[y][b]+g[a][x]<1:
                        for i in range(10-abs(a-b)):
                            g[a-min(a,b)+i][b-min(a,b)+i]=f
            elif c:
               f=c
    return[[c-5and c for c in r]for r in g]
