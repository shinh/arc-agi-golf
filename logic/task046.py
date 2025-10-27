def p(g):
 # align anchors
 r=[];v=0;s=[];z=0,0,0
 for c in*zip(*g),z:
  if c>z:s+=c,
  elif s:
   l=(s[0]+(5,)).index(5)%3
   c=max(n for t in s for n in t if n-5)
   r+=[[(n==5)*c or n for n in(z+t+z)[l-v+3:][:3]]for t in s]
   v+=(s[-1]+(5,)).index(5)%3-l;s=[]
 return[*zip(*r)]
