def p(g):
 #diag mirror/mode
 a=sum(g,[]);r=range(21);return[[(a[0],g[i][j]or g[j][i]or max({*a}-{0},key=a.count))[i!=j]for j in r]for i in r]

