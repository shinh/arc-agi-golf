def p(g):
 a=[[0]+r+[0]for r in g];n=len(a)+2;a=[[0]*n]+a+[[0]*n]
 def F(i,j):
  a[i][j]=-v
  for di in-1,0,1:
   for dj in-1,0,1:
    di|dj and a[i+di][j+dj]==v and F(i+di,j+dj)
  a[p-i][j],a[i][q-j],a[p-i][q-j]=t;a[i][j]=v
 for c in range(1,n-1):
  for f in range(1,n-1):
   for d in-1,1:
    for e in-1,1:
     v=a[c][f];t=a[c-d][f],a[c][f-e],a[c-d][f-e]
     if v and len({v,*t})>3:
      p,q=2*c-d,2*f-e;F(c,f)
 return[a[i][1:-1]for i in range(1,n-1)]