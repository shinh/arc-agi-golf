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
                    a,b,c,d=min(x),max(x),min(y),max(y);t=[[0]*(d-c+1)for _ in r(b-a+1)]
                    for x,y,u in C:R[x][y]=0;t[x-a][y-c]=u
                    m=max(z,key=z.count)
                    for k in r(8):
                        a,b=len(t),len(t[0])
                        for i in r(h-a+1):
                            for j in r(w-b+1):
                                if all((u:=t[x][y])in(0,m)or R[i+x][j+y]==u for x in r(a)for y in r(b)):
                                    for x in r(a):
                                        for y in r(b):
                                            if(u:=t[x][y]):R[i+x][j+y]=u
                        t=[*zip(*t[::-1])]
                        if k==3:t=t[::-1]
    return R
