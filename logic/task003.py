# extend grid depending on middle rows then double colors
p=lambda g:[[c*2 for c in r]for r in g+g[(g[1]!=g[4])*2:][:3]]
