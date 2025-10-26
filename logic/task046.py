def p(g):
 # align anchors
 r=[];v=0;s=[];z=0,0,0
 for c in (*zip(*g),z):
  if c>z:s+=c,
  elif s:
   l=5 in s[0]and s[0].index(5)
   c=max(n-5*(n==5)for t in s for n in t)
   r+=[[(n==5)*c or n for n in(z+t+z)[l-v+3:l-v+6]]for t in s]
   v-=l-(5 in s[-1]and s[-1].index(5));s=[]
 return[*zip(*r)]
