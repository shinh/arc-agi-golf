def p(g):
    # recolor 3s by shape
    h=len(g);w=len(g[0]);D=1,0,-1,0,0,1,0,-1
    for y in range(h):
        for x in range(w):
            if g[y][x]-3:continue
            C=[(y,x)];g[y][x]=0
            # flood fill component
            for y,x in C:
                for i in 0,2,4,6:
                    ny=y+D[i];nx=x+D[i+1]
                    if h>ny>=0<=nx<w and g[ny][nx]==3:g[ny][nx]=0;C+=[(ny,nx)]
            n=t=0
            # count endpoints and crossings
            for y,x in C:a=(y+1,x)in C;b=(y-1,x)in C;c=(y,x+1)in C;d=(y,x-1)in C;n+=a+b+c+d==1;t+=(a|b)and(c|d)
            c=(2,[6,1][t<2])[n<3]
            for y,x in C:g[y][x]=c
    return g
