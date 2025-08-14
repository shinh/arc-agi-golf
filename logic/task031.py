# 69
# p=lambda g,n=79:-n*g or p([*map(list,zip(*g[any(g[-1])-2::-1]))],n-1)
# 68 - AI found this
#p=lambda g,f=lambda g:zip(*filter(any,g)):[*map(list,f(f(f(f(g)))))]
# 62 two iter is enough
p=lambda g,f=lambda g:zip(*filter(any,g)):[*map(list,f(f(g)))]
