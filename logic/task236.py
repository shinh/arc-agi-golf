# compare top with bottom ignoring middle row
p=lambda g:[[3*((a>0)^(b>0))for a,b in zip(*s)]for s in zip(g,g[5:])]
