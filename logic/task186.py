def p(g):
    a=[v for r in g for v in r];n=a.count(1);c=0
    o=[[c]*3 for _ in range(3)]
    for i in range(min(n,3)):o[0][i]=2
    if n==4:o[1][1]=2
    return o
