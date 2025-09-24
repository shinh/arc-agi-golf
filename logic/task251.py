# rotate fill
p=lambda g,n=63:-n*g or p([[(b or a&1,b^(b<2))[n<1]for a,b in zip((1,)+r,r)]for r in zip(*g[::-1])],n-1)
