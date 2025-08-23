def p(j):
 #max 2s
 #scan corners to crop block
 return max((str(a:=[R[x:x+(*r[x:],0).index(0)]for R in j[y:y+(*[*zip(*j)][x][y:],0).index(0)]]).count('2'),a)for y,r in enumerate(j)for x,v in enumerate(r)if v*(y*j[y-1][x]<1)*(x*r[x-1]<1))[1]
