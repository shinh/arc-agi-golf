# row/col majority colors
p=lambda g:(z:=[*zip(*g)],i:=sum(len({*r})for r in z)<sum(len({*r})for r in g),(o:=[[max(r,key=r.count)]*len(r)for r in(g,z)[i]]))and(o,[*zip(*o)])[i]
