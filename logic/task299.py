# cross row of 2 and column of 8
# x%6-x+2 is +2 for 0 and -4 for 8
p=lambda g:[[(x,2+x%6)[2in r]for x in g[0]]for r in g]
