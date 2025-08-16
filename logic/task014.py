def p(g):# crop rare color
 b=sum(g,[]);c=min({*b}-{0},key=b.count);return[*map(list,zip(*[r for r in zip(*[r for r in g if c in r]) if c in r]))]
