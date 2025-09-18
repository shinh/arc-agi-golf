# paste cropped pattern over 8s
def p(g):
    a=b=9;c=d=0;R=range
    for y in R(10):
        for x in R(10):
            if g[y][x]%8:a=min(a,x);b=min(b,y);c=max(c,x);d=max(d,y)
    h=d-b+1;w=c-a+1;p=[r[a:c+1]for r in g[b:d+1]];o=[[0]*10 for _ in R(10)]
    for y in R(11-h):
        for x in R(11-w):
            if all((g[y+i][x+j]==8)==(p[i][j]>0)for i in R(h)for j in R(w)):
                for i in R(h):o[y+i][x:x+w]=p[i]
    return o
