def p(g):
    def f(b):
        if all(v==5 for r in b for v in r):return 2
        r1,r2=b[1],b[2];t=b[0]==b[3]==[5]*4
        if r1==r2==[5,0,0,5] and t:return 8
        if r1==r2==[0,5,5,0] and t:return 3
        return 4
    cs=[]
    for s in(0,5,10):cs.append(f([r[s:s+4] for r in g[:4]]))
    return[[c]*3 for c in cs]
