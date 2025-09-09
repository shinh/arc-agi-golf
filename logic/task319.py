def p(g):
    # compare border mini to shapes
    F=sum(g,[]);b=max(F,key=F.count)
    for c in range(10):
        f=lambda g:[*zip(*([[b,c][q==c]for q in r]for r in g if c in r))]
        o=f(f(g))
        if o and c!=b:
            for y in range(-len(o)*2,len(g)-3):
                for x in range(-len(o[0])*2,len(g[0])-3):
                    for q in range(10):
                        ok=1;cnt=0
                        for dy in range(len(o)*2):
                            for dx in range(len(o[0])*2):
                                ny=y+dy;nx=x+dx
                                if 0<=ny<len(g)and 0<=nx<len(g[0]):
                                    if(o[dy//2][dx//2]==c)!=(g[ny][nx]==q):ok=0
                                    if g[ny][nx]==q:
                                        cnt+=1
                        if ok and cnt==F.count(q)>0and q!=c:
                            return o
    return g