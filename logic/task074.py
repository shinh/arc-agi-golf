# orbit mins
p=lambda a,r=range(30):[[min(a[x][y]for X in(j,i)for x in(X,31-X)for y in(i+j-X,31-i-j+X)if x<30>y)for j in r]for i in r]
