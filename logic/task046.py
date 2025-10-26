def p(g):
 R=[];v=0;s=[]
 for c in(*zip(*g),0):
  if c and any(c):s+=c,
  elif s:
   c=max(n%5and n for t in s for n in t);l=5 in s[0] and s[0].index(5)
   R+=[tuple((0<=y+l-v<3 and ((t[y+l-v]==5 and c)or t[y+l-v]))or 0 for y in(0,1,2))for t in s]
   v+=(5 in s[-1] and s[-1].index(5))-l;s=[]
 return [*zip(*R)]