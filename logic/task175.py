def p(g):
 # mirror diag & fill zeros with most common color
 a=sum(g,[]);m=max({*a}-{0},key=a.count);r=range(21);return[[a[0]*(i==j)or g[i][j]or g[j][i]or m for j in r]for i in r]

