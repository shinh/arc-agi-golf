# 90
# rotate off 1 borders, then clear remaining 1s
p=lambda g,t=63:-t*[[g*(g>1)for g in g]for g in g]or p([*zip(*g[2>max(g[0]):][::-1])],t-1)
