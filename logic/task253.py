# rotate grid to reuse L pattern detection

def p(j):
 k=[]
 for _ in[0]*4:
  k+=[next((a for r,s in zip(j,j[1:])for a,b,d in zip(r,r[1:],s)if a==b==d>0),0)]
  j=[*zip(*j[::-1])]
 a,d,c,b=k
 return[[a,a,b,b],[a,0,0,b],[d,0,0,c],[d,d,c,c]]
