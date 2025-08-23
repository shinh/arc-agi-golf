def p(g):
    # rotate/flip
    E=enumerate;R=range
    p=[[0]*25,*[[0]+r+[0]for r in g],[0]*25]
    x,y=zip(*[(i,j)for i,r in E(p)for j,v in E(r)if v==1])
    r=[row[min(y):max(y)+1]for row in p[min(x):max(x)+1]]
    for _ in R(4):
        for t in (r,[k[::-1]for k in r]):
            for i in R(26):
                for j in R(26):
                    try:
                        if all((v-4)*(v-1)or p[i+x][j+y]==(v==4)*4 for x,row in E(t)for y,v in E(row)):
                            for x,row in E(t):p[i+x][j:j+len(row)]=row
                    except:0
        r=[*zip(*r[::-1])]
    return[row[1:-1]for row in p[1:-1]]

