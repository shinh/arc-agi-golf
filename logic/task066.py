# connect 3 to 2 around blocks
def p(g):
    h=len(g);w=len(g[0]);s=sum(g,[])
    ry,rx=divmod(s.index(2),w)
    j=s.index(3);sy,sx=divmod(k:=s.index(3,j+1),w);dy,dx=k-j==w,k-j==1
    B=g;b=9
    for dy,dx in(dy,dx),(-dy,-dx):
        ny,nx=sy,sx;o=[*map(list,g)];q=0
        while q<9 and h>ny>-1<nx<w and (t:=g[ny][nx])-2:
            if t==8:q+=1;ny-=dy;nx-=dx;dy,dx=(([-1,1][ry>ny],0),(0,[-1,1][rx>nx]))[dy]
            else:o[ny][nx]=3;ny+=dy;nx+=dx
        if t==2 and q<b:b=q;B=o
    return B
