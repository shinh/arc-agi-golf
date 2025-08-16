def p(g):
    # rotate/flip
    R=range;E=enumerate;C={*sum(g,[])}
    def b(c):
        t=[(i,j)for i,r in E(g)for j,v in E(r)if v==c]
        if t:x,y=zip(*t);return max(max(x)-min(x),max(y)-min(y))+1
        return 99
    a=min(C,key=b)
    d=min(C-{a},key=lambda c:sum(r.count(c)for r in g))
    p=[[0]*25,*[[0]+r+[0]for r in g],[0]*25]
    x,y=zip(*[(i,j)for i,r in E(p)for j,v in E(r)if v==a]);si=min(x);ei=max(x);sj=min(y);ej=max(y);r=[row[sj:ej+1]for row in p[si:ei+1]]
    for _ in R(4):
        for t in r,[row[::-1]for row in r]:
            h=len(t);w=len(t[0])
            for i in R(26-h):
                for j in R(26-w):
                    if all((v-d)*(v-a) or p[i+x][j+y]==(v==d)*d for x,row in E(t)for y,v in E(row)):
                        for x,row in E(t):p[i+x][j:j+w]=row
        r=[*zip(*r[::-1])]
    return[row[1:-1]for row in p[1:-1]]
