def p(g):
    a,b=g
    r0=[[b[i],a[i]][i%2==0]for i in range(len(a))]
    r1=[[a[i],b[i]][i%2==0]for i in range(len(a))]
    return [r0,r1]
