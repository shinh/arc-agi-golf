# infer tile by using period.
def p(g,p=1):
    # Find the period.
    for r in g:
        while all(r)*(r[:-p]!=r[p:]):p+=1
    # Complement the first square.
    R=range(18)
    for y in R:
        for x in R:g[y%p][x%p]|=g[y][x]
    # Complement the rest.
    #return[(g[y%p][:p]*9)[:18]for y in R]
    return[(g[y%p][:p]*9)[:18]for y in R]
