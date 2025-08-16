def p(E):#1 near 5
 n=len(E);r=range(n);return[[any(0<=i+d<n>j+e>=0<=E[i+d][j+e]==5 for d in(-1,0,1)for e in(-1,0,1))for j in r]for i in r]
