#3x3 5-union
p=lambda g,a=(1,0,-1):[[max(g[k//11-i][k%11-j]for k in range(121)if g[k//11][k%11]==5)for j in a]for i in a]

