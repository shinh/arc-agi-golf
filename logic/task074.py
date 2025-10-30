# orbit mins
p=lambda a,r=range(30):[[min(min(a[x][y],a[y][x])for x in(i,31-i)for y in(j,31-j)if x<30>y)for j in r]for i in r]
