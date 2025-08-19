# 240
def p(g):
    # detect repeat and fill zero box
    p=1
    for r in g+[*zip(*g)]:
        if len({*r})>1>r.count(0):
            while(r[:p]*9)[:len(r)]!=r:p+=1
            break
    return[[g[y%p][x%p]or g[y%p+p][x%p+p]for x,c in enumerate(r)if c<1]for y,r in enumerate(g)if 0in r]
