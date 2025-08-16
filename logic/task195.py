# 204
# crop then expand fractal
def p(g):
 g=[*eval('zip(*filter(any,'*2+'g))))')];r=range(9);return[[g[i*3%9][j*3%9]&g[i-i%3][j-j%3]for j in r]for i in r]
