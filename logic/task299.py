# cross row of 2 and column of 8
# There should be a better formula
p=lambda g:[[[0,2,8,4][(g[0][x]>0)*2+(2 in r)] for x in range(6)]for r in g]
