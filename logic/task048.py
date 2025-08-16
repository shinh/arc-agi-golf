# flood fill through 8s from first 2 block
# detect connection to another 2 block

def p(g):
 w=len(g[0])+2
 s=sum(([0]+r+[0]for r in g),[0]*w)+[0]*w
 i=s.index(2);q=[]
 for d in 0,1,w,w+1:s[i+d]=1;q+=i+d,
 while q:
  i=q.pop()
  for d in-1,1,-w,w:
   v=s[i+d]
   if v==2:return[[8]]
   if v==8:s[i+d]=1;q+=i+d,
 return[[0]]

