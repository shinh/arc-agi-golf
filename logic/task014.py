def p(g):# crop rare color
 b=sum(g,[]);f=lambda r,c=min({*b}-{0},key=b.count):c in r;return[*zip(*filter(f,zip(*filter(f,g))))]
