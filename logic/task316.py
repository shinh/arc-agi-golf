# first nonzero per nonempty column, zigzag
p=lambda m:((v:=[s for c in zip(*m)if(s:=sum(c))]+[0]*9)[:3],v[5:2:-1],v[6:9])

