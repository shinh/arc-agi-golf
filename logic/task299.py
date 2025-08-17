# cross row of 2 and column of 8
# better formula?
p=lambda g:[[x+(2in r)*(2-6*x//8)for x in g[0]]for r in g]
