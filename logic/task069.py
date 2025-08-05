def p(g):
    a=b=10;c=d=0
    for y,r in enumerate(g):
        for x,v in enumerate(r):
            if v and v-8:
                if x<a:a=x
                if x>c:c=x
                if y<b:b=y
                if y>d:d=y
    p=[r[a:c+1] for r in g[b:d+1]];h=len(p);w=len(p[0]);o=create(10,10)
    for y in range(10-h+1):
        for x in range(10-w+1):
            if all((g[y+i][x+j]==8)==(p[i][j]>0) for i in range(h) for j in range(w)):
                for i in range(h):o[y+i][x:x+w]=p[i]
    return o
