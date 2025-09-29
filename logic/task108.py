# 64
p=lambda g,r=range(20):[[g[y>>1|1][x>>1|1]for x in r]for y in r]
# 68
# p=lambda g,z=-1:g*z or p([[*zip(*g)][y>>1|1]for y in range(20)],z+1)
