R=range
def p(g):
    h=len(g);w=len(g[0])
    for y in R(h):
        for x in R(w):
            if g[y][x]<1:continue
            q=[(y,x)];g[y][x]*=-1;s=[(y,x)];m=[0]*4
            while q:
                i,j=q.pop();d=-g[i][j];m[d]+=1
                for Y,X in(1,0),(-1,0),(0,1),(0,-1):
                    Y+=i;X+=j
                    if h>Y>=0<=X<w and g[Y][X]>0:
                        g[Y][X]*=-1;q+=[(Y,X)];s+=[(Y,X)]
            L=2+(m[2]>m[3]);M=5-L
            for a,b in s:
                if -g[a][b]==L:break
            for Y,X in(-1,0),(1,0),(0,-1),(0,1):
                if (a+Y,b+X)not in s:break
            n=0;i,j=a-Y,b-X
            while(i,j)in s:n+=1;i-=Y;j-=X
            if Y:
                t=[0,a-n][Y>0];B=[a+n,h-1][Y>0];l=max(0,b-n);r=min(w-1,b+n)
            else:
                t=max(0,a-n);B=min(h-1,a+n);l=(b-n)*(X>0);r=(b+n)*(X<0)+(w-1)*(X>0)
            for i in R(t,B+1):g[i][l:r+1]=[-M]*(r-l+1)
            i,j=a,b
            while h>i>=0<=j<w:
                if t<=i<=B and l<=j<=r:g[i][j]=-L
                i+=Y;j+=X
    return[[abs(c)for c in r]for r in g]
