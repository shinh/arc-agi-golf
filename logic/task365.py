def p(j):
 #max 2s
 return max((str(a).count('2'),a)for y,r in enumerate(j)for x,v in enumerate(r)if v*(y<1or j[y-1][x]<1)*(x<1or r[x-1]<1)for a in[[R[x:x+(*r[x:],0).index(0)]for R in j[y:y+(*[*zip(*j)][x][y:],0).index(0)]]])[1]
