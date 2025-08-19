# 186
def p(g,p=1):
    # detect repeat and fill zero box
    for r in[*zip(*g)]+g:
        if 0not in r:
            while(r[:p]*9)[:len(r)]!=r:p+=1
    return[[g[y%p][x%p]or g[y%p][x%p+p]for x,c in enumerate(r)if c<1]for y,r in enumerate(g)if 0in r]
