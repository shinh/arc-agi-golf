def p(g):
    o=create(4,4);d={}
    for y,r in enumerate(g):
        for x,v in enumerate(r):
            if v:d.setdefault(v,[]).append((y,x))
    for k,pts in d.items():
        ys=[y for y,_ in pts];xs=[x for _,x in pts]
        s={(y-min(ys),x-min(xs)) for y,x in pts}
        if s=={(0,0),(0,1),(1,0)}:b=(0,0)
        elif s=={(0,0),(0,1),(1,1)}:b=(0,2)
        elif s=={(0,0),(1,0),(1,1)}:b=(2,0)
        else:b=(2,2)
        for dy,dx in s:o[b[0]+dy][b[1]+dx]=k
    return o
