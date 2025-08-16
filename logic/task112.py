def p(g):
    # mirror each color around the center of the only 2x2 block
    h=len(g);w=len(g[0]);f=sum(g,[])
    for i,v in enumerate(f):
        if v and f.count(v)==4:S=i//w*2+1;T=i%w*2+1;break
    for i,c in enumerate(f):
        if c:
            for Y in i//w,S-i//w:
                for X in i%w,T-i%w:
                    if h>Y>-1 and w>X>-1:g[Y][X]=c
    return g
