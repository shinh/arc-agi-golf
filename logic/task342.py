def p(g):
 # fill corners from quadrants
 s=sum(g,[]);o=create(10,10);r,c=divmod(s.index(8),10)
 for i,v in enumerate(s):
  if v%8 and((y:=i//10)<r or y>r+1)and((x:=i%10)<c or x>c+1):o[r+(y>r+1)][c+(x>c)]=v
 return o
