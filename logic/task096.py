def p(g):
    show(g,"input")
    pats=[]
    b=0
    H=len(g)
    W=len(g[0])
    max_l=0
    for c in range(9):
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
        if cnt>100:
            b=c
            continue
        if ey>=0:
            pat=None
            for l in range(1,30,2):
                for oy in range(sy-ey-l,1):
                    for ox in range(sx-ex-l,1):
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
                            pat=(-l,c,sy,sx,ey,ex,oy,ox,cnt)
                            print(f"Pattern found: {c} at ({sy},{sx}) to ({ey},{ex}) with offset ({oy},{ox}) and length {l} cnt={cnt}")
                if pat is not None:
                    pats.append(pat)
                    max_l=max(max_l,l)
                    break
            if pat is None:
                # TODO: Fix this!
                raise RuntimeError(f"Patter not found!!! {c} cnt={cnt}")

    # So now we have sx+ox and sy+oy and l, we can finish the pattern.
    o=create(max_l,max_l)
    for l,c,sy,sx,ey,ex,oy,ox,cnt in sorted(pats):
        l=-l
        d=(max_l-l)//2
        for by in range(l):
            for bx in range(l):
                y=oy+sy+by
                if y<0:y=oy+sy+l-by-1
                if y>=H:y=oy+sy+l-by-1
                x=ox+sx+bx
                if x<0:x=ox+sx+l-bx-1
                if x>=W:x=ox+sx+l-bx-1
                o[by+d][bx+d]=g[y][x]
        show(o,f"output l={l}")

    show(o,"output")
    return o
