def p(g):# crop rare color
 b=sum(g,[]);return[*zip(*filter(f:=lambda r,c=min({*b}-{0},key=b.count):c in r,zip(*filter(f,g))))]
