def p(g):# BFS region then copy scaled with rot90
    #show(g,"input")
    #print(f'start {len(g)=} {len(g[0])=}')
    B=g[-1][0];h=len(g);w=len(g[0]);R=range
    for y in R(h):
        for x in R(w):
            if g[y][x]==B:continue
            q=[(y,x)];c=[]
            for a,b in q:
                for dy in-1,0,1:
                    for dx in-1,0,1:
                        if dy|dx and-1<(ny:=a+dy)<h>-1<(nx:=b+dx)<w and g[ny][nx]-B and(ny,nx)not in q:
                            q+=[(ny,nx)]
                            c+=g[ny][nx],
            if len({*c})<2:continue

            my,mx=zip(*q)
            ly=max(my)-min(my)+1
            lx=max(mx)-min(mx)+1

            #y=min(my)
            x=min(mx)

            bc=max(c,key=c.count)

            #print(f'box {y=} {x=} {ly=} {lx=} {bc=} {B=}')

            o=[r[:]for r in g]
            for t in R(4):
                for s in R(1,5):
                    for ty in R(len(o)-s*ly+1):
                        for tx in R(len(o[0])-s*lx+1):
                            if all(o[ty+dy][tx+dx]==[q:=g[y+dy//s][x+dx//s],B][q==bc]for dy in R(s*ly)for dx in R(s*lx)):
                                #print(f"found {ty=} {tx=} {s=}")
                                #show(o,"found",(ty,tx))
                                for dy in R(s*ly):
                                    for dx in R(s*lx):
                                        o[ty+dy][tx+dx]=g[y+dy//s][x+dx//s]
                o=[*map(list,zip(*o[::-1]))]
            return o
