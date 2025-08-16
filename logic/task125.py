def p(g):
    # flood each 6 region and draw padded box
    w=15;o=[r[:]for r in g]
    for y in range(w):
        for x in range(w):
            if g[y][x]==6:
                s=[(y,x)];Y=[y];X=[x];g[y][x]=0
                while s:
                    y,x=s.pop()
                    for ny,nx in((y+1,x),(y-1,x),(y,x+1),(y,x-1)):
                        if w>ny>=0<=nx<w and g[ny][nx]==6:
                            s+=[(ny,nx)];g[ny][nx]=0;Y+=ny,;X+=nx,
                a=max(min(Y)-1,0);b=min(max(Y)+2,w);c=max(min(X)-1,0);d=min(max(X)+2,w)
                for y in range(a,b):
                    for x in range(c,d):
                        if y in(a,b-1)or x in(c,d-1):o[y][x]=3
                        elif o[y][x]-6:o[y][x]=4
    return o

