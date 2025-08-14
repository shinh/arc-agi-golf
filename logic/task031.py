# 69
p=lambda g,n=79:-n*g or p([*map(list,zip(*g[any(g[-1])-2::-1]))],n-1)
