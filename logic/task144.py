# compare top and bottom 4x4 blocks
p=lambda g:[[3*(a+b<1)for a,b in zip(*x)]for x in zip(g,g[5:])]
