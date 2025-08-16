def p(g):
    # flood fill each 6-cluster then box it
    R=range(15);v=set();t=((1,0),(-1,0),(0,1),(0,-1))
    for y in R:
        for x in R:
            if g[y][x]==6 and (y,x)not in v:
                s=[(y,x)];Y=[];X=[]
                while s:
                    y,x=s.pop()
                    if(y,x)in v:continue
                    v.add((y,x));Y+=y,;X+=x,
                    for a,b in t:
                        c=y+a;d=x+b
                        if 0<=c<15 and 0<=d<15 and g[c][d]==6:s+=[(c,d)]
                a=max(min(Y)-1,0);b=min(max(Y)+2,15);c=max(min(X)-1,0);d=min(max(X)+2,15)
                for Y in range(a,b):
                    for X in range(c,d):
                        g[Y][X]=3 if Y in(a,b-1)or X in(c,d-1)else 6-2*(g[Y][X]!=6)
    return g
