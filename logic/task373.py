def p(g):
    a,b=g
    r0=[a[i] if i%2==0 else b[i] for i in range(len(a))]
    r1=[b[i] if i%2==0 else a[i] for i in range(len(a))]
    return [r0,r1]
