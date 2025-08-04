def p(g):
    show(g,"input")
    pats=[]
    b=0
    H=len(g)
    W=len(g[0])
    for c in range(9):
        if (g[0][0]==c)+(g[-1][0]==c)+(g[0][-1]==c)+(g[0][-1]==c)>=3:
            b=c
        sy=sx=999
        ey=ex=-1
        cnt=0
        for y in range(H):
            for x in range(W):
                if g[y][x]==c:
                    sy=min(sy,y)
                    sx=min(sx,x)
                    ey=max(ey,y)
                    ex=max(ex,x)
                    cnt+=1
        if ey>=0:
            pat=None
            for l in range(1,30,2):
                for oy in range(sy-ey,1):
                    for ox in range(sx-ex,1):
                        cnt2=0
                        for y in range(oy+sy,min(oy+sy+l,H)):
                            for x in range(ox+sx,min(ox+sx+l,W)):
                                if y<0 or x<0:
                                    continue
                                if g[y][x]==c:
                                    if y!=oy+sy and y!=min(oy+sy+l,H)-1 and x!=ox+sx and x!=min(ox+sx+l,W)-1:
                                        cnt2=-999
                                    else:
                                        cnt2+=1


                        if cnt==cnt2:
                            pat=(c,sy,sx,ey,ex,oy,ox,l,cnt)
                            print(f"Pattern found: {c} at ({sy},{sx}) to ({ey},{ex}) with offset ({oy},{ox}) and length {l} cnt={cnt}")
                if pat is not None:
                    pats.append(pat)
                    break

    return g
