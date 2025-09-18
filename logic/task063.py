# fill rows/cols of zeros with 3
def p(g):t=(*zip(*g),);return[[3if 0<i<len(g)-1>j>0 and any(r[1:-1])*any(t[j][1:-1])<1 else v for j,v in enumerate(r)]for i,r in enumerate(g)]

