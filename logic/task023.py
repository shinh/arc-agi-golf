def p(g):
    h=len(g);w=len(g[0])
    a=[[0]*(w+2) for _ in range(h+2)]
    for i,r in enumerate(g):
        for j,v in enumerate(r):a[i+1][j+1]=v
    b=[[0]*(w+2) for _ in range(h+2)]
    R=lambda m:[list(x) for x in zip(*m[::-1])]
    for _ in range(5):
        for _ in range(4):
            for i in range(len(a)-3):
                for j in range(len(a[0])-3):
                    if a[i+1][j+1]==a[i+1][j+2]==a[i+2][j+1]==a[i+2][j+2]==5 and all(a[i][j+k]==0 for k in range(4)) and a[i+1][j]==a[i+2][j]==a[i+3][j]==a[i+3][j+1]==a[i][j+3]==a[i+1][j+3]==0:
                        for di in(1,2):
                            for dj in(1,2):
                                b[i+di][j+dj]=8;a[i+di][j+dj]=0
            for i in range(1,len(a)-2):
                for j in range(1,len(a[0])-1):
                    if a[i][j]==5 and a[i][j-1]==a[i][j+1]==a[i-1][j]==0:
                        for k in range(3):b[i+k][j]=2;a[i+k][j]=0
            a=R(a);b=R(b)
    return [r[1:-1] for r in b[1:-1]]
