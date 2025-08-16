# scale grid by count of colored cells
def p(g):s=sum;n=s(map(bool,s(g,[])));return s([[s(([x]*n for x in r),[])]*n for r in g],[])
