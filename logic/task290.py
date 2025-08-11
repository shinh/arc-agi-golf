# 165
def p(g):
    f=sum(g,[])
    f.sort(key=f.count)
    a=list(set(f))[1:3]
    o=[]
    for r in g:
        n=[]
        for x in range(len(r)):
            if r[x]:
                n+=a[r[x]==a[0]],
        if n:
            o+=n,
    return o
