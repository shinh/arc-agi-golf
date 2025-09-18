# connect 3 to 2 around blocks
def p(g):
    h=len(g);w=len(g[0]);s=sum(g,[])
    ry,rx=divmod(s.index(2),w)
    j=s.index(3);sy,sx=divmod(k:=s.index(3,j+1),w);dy,dx=divmod(k-j,w)
    b=9;B=g
    for dy,dx in(dy,dx),(-dy,-dx):
        q=0;ny,nx=sy,sx;o=[r[:]for r in g]
        while q<9 and h>ny>-1<nx<w and (t:=g[ny][nx])-2:
            if t-8:o[ny][nx]=3;ny+=dy;nx+=dx
            else:q+=1;ny-=dy;nx-=dx;dy,dx=(((-1,1)[ry>ny],0),(0,(-1,1)[rx>nx]))[dy]
        if t==2 and q<b:B=o;b=q
    return B
