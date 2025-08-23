# extend diagonals
def p(g,e=enumerate):X=[[0]*6for _ in g+g];[X[r+i].__setitem__(c+i,v)for r,R in e(g)for c,v in e(R)for i in range(6-max(r,c))if v];return X
