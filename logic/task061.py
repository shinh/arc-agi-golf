# infer tile by using period.
def p(g,p=1):
    # Find the period.
    for r in g:
        while all(r)*(r[:-p]!=r[p:]):p+=1
    # Complement the first square.
    for y,r in enumerate(g):
        for x,c in enumerate(r):
            if c:
                g[y%p][x%p]=c
    # Complement the rest.
    return[[g[y%p][x%p]for x,c in enumerate(r)]for y,r in enumerate(g)]
