# merge halves
p=lambda g:[[*map(max,*rs)]for rs in zip(g,g[6:])]
