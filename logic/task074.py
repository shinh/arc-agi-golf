r=range(30)
s=lambda v:(v,)if v<2 else(v,31-v)
# orbit mins
def p(a):
 return[[min(a[x][y]for X,Y in((i,j),(j,i))for x in s(X)for y in s(Y))for j in r]for i in r]
