# rotate off 1 borders, then clear remaining 1s
p=lambda g,t=64:t and p([*zip(*g[2>max(g[0]):][::-1])],t-1)or[[g*(g>1)for g in g]for g in g]
