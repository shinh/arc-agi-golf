# flood fill through 8s from first 2 block
# detect connection to another 2 block

def p(g):
 w=len(g[0])+2;s=[0]*w
 for r in g:s+=0,*r,0
 s+=[0]*w
 q=[i:=s.index(2),i+1,i+w,i+w+1]
 for j in q:s[j]=1
 for i in q:
  for j in i-1,i+1,i-w,i+w:
   if 2&s[j]:return(8,),
   if 8&s[j]:s[j]=1;q+=j,
 return(0,),

