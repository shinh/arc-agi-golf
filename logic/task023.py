def p(g):
    # rotate and paint blocks
    w=len(g[0])+2;a=[[0]*w]+[[0]+r+[0]for r in g]+[[0]*w];b=[[0]*w for _ in a];S=lambda m:[list(x)for x in zip(*m[::-1])];R=range
    for _ in[0]*8:
        for i in R(len(a)-3):
            for j in R(len(a[0])-3):
                if sum(a[i+1][j+1:j+3]+a[i+2][j+1:j+3])>19>sum(a[i][j:j+4]+a[i+1][j:j+4:3])*5:
                    b[i+1][j+1:j+3]=b[i+2][j+1:j+3]=8,8;a[i+1][j+1:j+3]=a[i+2][j+1:j+3]=0,0
        for i in R(1,len(a)-2):
            for j in R(1,len(a[0])-1):
                if a[i][j]==5>a[i][j-1]+a[i][j+1]+a[i-1][j]:
                    b[i][j]=b[i+1][j]=b[i+2][j]=2;a[i][j]=a[i+1][j]=a[i+2][j]=0
        a,b=S(a),S(b)
    return[r[1:-1]for r in b[1:-1]]
