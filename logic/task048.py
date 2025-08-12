# rotate grid to flow right through 8s from first 2 block
# to detect connection to another 2 block using rotation

def p(g):
 w=len(g[0]);s=sum(g,[]);i=s.index(2);f=0
 for d in range(4):g[i//w+d//2][i%w+d%2]=1
 for _ in range(64):
  for r in g:
   for j in range(len(r)-1):
    if r[j]==1<r[j+1]:f|=r[j+1]<3;r[j+1]=1
  if f:return[[8]]
  g=[list(r)for r in zip(*g[::-1])]
 return[[0]]
