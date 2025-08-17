# connect 3 to 2 around blocks
def p(g):
    h=len(g);w=len(g[0]);dy=dx=0
    for y in range(h):
        for x in range(w):
            t=g[y][x]
            if t==2:ry=y;rx=x
            elif t==3:
                if y and g[y-1][x]==3:dy=1;sy=y;sx=x
                elif x and g[y][x-1]==3:dx=1;sy=y;sx=x
    b=9;B=g
    for dy,dx in(dy,dx),(-dy,-dx):
        ny,nx=sy,sx;o=[r*1for r in g];q=0
        while q<9 and h>ny>=0<=nx<w:
            t=g[ny][nx]
            if t==2:
                if q<b:b=q;B=o
                break
            if t==8:
                q+=1;ny-=dy;nx-=dx
                if dy:dy=0;dx=[-1,1][rx>nx]
                else:dy=[-1,1][ry>ny];dx=0
            else:o[ny][nx]=3;ny+=dy;nx+=dx
    return B
