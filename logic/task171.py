def p(g):# border
    return[(x:=[8]*(w:=len(g[0]))),*[[8,*[0]*(w-2),8]]*(len(g)-2),x]
