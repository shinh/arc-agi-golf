# flood fill through 8s from first 2 block
# detect connection to another 2 block

def p(g):
 w=len(g[0])+2;s=[0]*w
 for r in g:s+=0,*r,0
 s+=[0]*w
 q=[i:=s.index(2),i+1,i+w,i+w+1]
 for d in q:s[d]=1
 for i in q:
  for d in-1,1,-w,w:
   if s[i+d]&2:return(8,),
   if s[i+d]&8:s[i+d]=1;q+=i+d,
 return(0,),

