# 146
def p(g,p=1):
    # detect repeat and fill zero box
    for r in g+[*zip(*g)]:
        while all(r)*(r[:-p]!=r[p:]):p+=1
    return[[max(r[x%p::p])for x,c in enumerate(r)if c<1]for r in g if 0in r]
