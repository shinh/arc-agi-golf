def p(g):
    k=sum(r[-1]==5 for r in g)
    for y,r in enumerate(g):
        for x,v in enumerate(r):
            if v and v-5:c=v;p=x
        if r.count(c)==10:s=y
    p-=k;s+=k
    o=create(10,10)
    for y in range(10):
        if y==s:o[y]=[c]*10
        else:o[y][p]=c
    return o
