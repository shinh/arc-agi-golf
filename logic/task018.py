# flood fill 4-color shapes, paste their pattern elsewhere using majority color as wildcard
def p(g):
    h,w=len(g),len(g[0]);R=[*map(list,g)];r=range
    def F(i,j):
        if-1<i<h and-1<j<w and(u:=g[i][j])>0:
            g[i][j]=0;return[(i,j,u)]+F(i+1,j)+F(i-1,j)+F(i,j+1)+F(i,j-1)
        return[]
    for i in r(h):
        for j in r(w):
            if g[i][j]:
                C=F(i,j);x,y,z=zip(*C)
                if len({*z})>3:
                    a,b,c,d=min(x),max(x)+1,min(y),max(y)+1
                    P=[(x-a,y-c,u)for x,y,u in C]
                    for x,y,_ in C:R[x][y]=0
                    m=max(z,key=z.count);H=b-a;W=d-c
                    for _ in'00':
                        for _ in'0000':
                            for I in r(h-H+1):
                                for J in r(w-W+1):
                                    if all(u==m or R[I+x][J+y]==u for x,y,u in P):
                                        for x,y,u in P:R[I+x][J+y]=u
                            H1=H;P=[(y,H1-1-x,u)for x,y,u in P];H,W=W,H1
                        P=[(H-1-x,y,u)for x,y,u in P]
    return R
