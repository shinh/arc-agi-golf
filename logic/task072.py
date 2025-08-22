# XOR top and bottom halves separated by a wall row
p=lambda g:[[(x!=y)*3for x,y in t]for t in map(zip,g,g[7:])]

