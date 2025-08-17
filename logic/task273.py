def p(g):
    # fill rectangles enclosed by 4s
    R=range(10)
    for y2 in R:
        for y1 in range(y2):
            if s:=[i for i in R if g[y1][i]==g[y2][i]==4]:
                a=s[0];b=s[-1]
                for r in g[y1+1:y2]:r[a+1:b]=[2]*~(a-b)
    return g
