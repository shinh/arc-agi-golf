def p(g):
 # fill corners from quadrants
 s=sum(g,[]);o=create(10,10);r,c=divmod(s.index(8),10)
 for i,v in enumerate(s):
  if v%8*(y:=i//10-r)*(y-1)*(x:=i%10-c)*(x-1):o[r+(y>1)][c+(x>0)]=v
 return o
