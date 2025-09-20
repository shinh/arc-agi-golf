# row/col majority colors
p=lambda g:(s:=lambda a:sum(map(len,map(set,a))),i:=s(z:=[*zip(*g)])<s(g),(o:=[[max(r,key=r.count)]*len(r)for r in(g,z)[i]]))and(o,[*zip(*o)])[i]
