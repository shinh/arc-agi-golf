# first nonzero per column zigzag
p=lambda m:((v:=list(map(sum,filter(sum,zip(*m))))+[0]*9)[:3],v[5:2:-1],v[6:9])
