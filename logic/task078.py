def p(g):
    for x in range(10):
        c=[r[x] for r in g];n=c.count(2)
        if n:
            c=[v for v in c if v-2]
            i=0
            for v in c:
                if v:i+=1
                else:break
            c[i:i]=[2]*n
            c+=10*[0]
            for y in range(10):g[y][x]=c[y]
    return g
