t={30,31}
r=range(30)
# orbit mins
p=lambda a:[[min(a[x][y]for X,Y in((i,j),(j,i))for x in{X,31-X}-t for y in{Y,31-Y}-t)for j in r]for i in r]
