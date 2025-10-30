# extend segments away/toward the wall by color
p=lambda g:(r:=g.index([5]*10),[_.__setitem__(x,v)for y in range(10)for x,v in enumerate(g[y])for _ in g[y:(None,r)[v>1]:1-2*((y<r)^(v-1))]*v],g)[2]
