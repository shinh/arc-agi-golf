# 69
# p=lambda g,n=79:-n*g or p([*map(list,zip(*g[any(g[-1])-2::-1]))],n-1)
# 68 - AI found this
# p=lambda g,f=lambda g:zip(*filter(any,g)):[*map(list,f(f(f(f(g)))))]
# 62 - two iters are enough
# p=lambda g,f=lambda g:zip(*filter(any,g)):[*map(list,f(f(g)))]
# 62 - loop
# p=lambda g,n=1:-n*g or p([*map(list,zip(*filter(any,g)))],n-1)
# 61 - expand
# p=lambda g:[*map(list,zip(*filter(any,zip(*filter(any,g)))))]
# 61 - eval
# p=lambda g:eval("[*map(list,"+"zip(*filter(any,"*2+"g)))))]")
# 56 - inner eval
p=lambda g:[*map(list,eval('zip(*filter(any,'*2+'g))))'))]
