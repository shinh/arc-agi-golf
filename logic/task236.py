# compare top with bottom ignoring middle row
p=lambda g:[[3*(a>0)^3*(b>0)for a,b in s]for s in map(zip,g,g[5:])]
