def p(g):# flood fill then expand
    h=len(g);w=len(g[0]);o=[r[:]for r in g]
    for i,r in enumerate(g):
        for j,v in enumerate(r):
            if v:
                a=v;b=0;g[i][j]=0;ps=[(i,j)];mn=mx=i;ln=rx=j
                for y,x in ps:
                    for Y,X in((y+1,x),(y-1,x),(y,x+1),(y,x-1)):
                        if h>Y>-1<X<w and (t:=g[Y][X]):
                            g[Y][X]=0;ps+=[(Y,X)];mn=min(mn,Y);mx=max(mx,Y);ln=min(ln,X);rx=max(rx,X)
                            if t!=a:b=t
                dh=mx-mn-1;dw=rx-ln-1
                for y in range(mn,mx+1):
                    for x in range(ln,rx+1):o[y][x]=a
                for y,x in ps:
                    for Y,X in((y-dh,x),(y+dh,x),(y,x-dw),(y,x+dw)):
                        if h>Y>-1<X<w:o[Y][X]=a
                for x in range(ln,rx+1):o[mn][x]=o[mx][x]=b
                for y in range(mn,mx+1):o[y][ln]=o[y][rx]=b
    return o
