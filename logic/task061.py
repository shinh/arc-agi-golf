# infer tile by using period.
def p(g,p=1):
    # Find the period.
    for r in g:
        while all(r)*(r[:-p]!=r[p:]):p+=1
    # Complement the first square.
    for y in range(18):
        for x in range(18):
            g[y%p][x%p]|=g[y][x]
    # Complement the rest.
    #return[(g[y%p][:p]*9)[:18]for y in range(18)]
    return([(r[:p]*9)[:18]for r in g[:p]]*9)[:18]
