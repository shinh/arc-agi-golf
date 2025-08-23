# 89
# rotate off 1 borders, then clear remaining 1s
p=lambda g,t=63:-t*eval(str(g).replace('1','0'))or p([*zip(*g[2>max(g[0]):][::-1])],t-1)
