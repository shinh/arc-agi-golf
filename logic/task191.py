def p(g):
    p=[[0]*25,*[[0]+r+[0]for r in g],[0]*25]
    x,y=zip(*[(i,j)for i,a in enumerate(p)for j,v in enumerate(a)if v==1]);r=[b[min(y):max(y)+1]for b in p[min(x):max(x)+1]]
    for _ in range(4):
        for t in r,r[::-1]:
            for i in range(26):
                for j in range(26):
                    if all(p[i+q:i+q+1]and p[i+q][j+w:j+w+1]==[v&4]for q,a in enumerate(t)for w,v in enumerate(a)):
                        for q,a in enumerate(t):p[i+q][j:j+len(a)]=a
        r=[*zip(*r[::-1])]
    return[b[1:-1]for b in p[1:-1]]