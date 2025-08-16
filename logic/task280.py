R=range
def p(g):
    # flood fill then frame
    h=len(g);w=len(g[0])
    for y in R(h):
        for x in R(w):
            if g[y][x]<1:continue
            q=[(y,x)];g[y][x]*=-1;m=[0]*4
            for i,j in q:
                m[-g[i][j]]+=1
                for Y,X in(i+1,j),(i-1,j),(i,j+1),(i,j-1):
                    if h>Y>=0<=X<w and g[Y][X]>0:
                        g[Y][X]*=-1;q+=[(Y,X)]
            L=2+(m[2]>m[3])
            for a,b in q:
                if -g[a][b]==L:break
            for Y,X in(-1,0),(1,0),(0,-1),(0,1):
                if (a+Y,b+X)not in q:break
            n=0;i,j=a-Y,b-X
            while(i,j)in q:n+=1;i-=Y;j-=X
            if Y:t=[0,a-n][Y>0];B=[a+n,h-1][Y>0];l=max(0,b-n);r=min(w-1,b+n)
            else:t=max(0,a-n);B=min(h-1,a+n);l=(b-n)*(X>0);r=(b+n)*(X<0)+(w-1)*(X>0)
            for i in R(t,B+1):g[i][l:r+1]=[L-5]*(r-l+1)
            while h>a>=0<=b<w:
                if t<=a<=B and l<=b<=r:g[a][b]=-L
                a+=Y;b+=X
    return[[abs(c)for c in r]for r in g]
