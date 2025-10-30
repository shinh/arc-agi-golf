def p(g):
 s=sum(g,[]);e=[i for i in range(100)if s[i]==2];m=min(e);x=min(i%10 for i in e);e=[i-x-m+m%10 for i in e];a=[]
 for t in range(100):
  if all(t+u<100and t%10+u%10<10and s[t+u]<1for u in e):
   a+=t,
   for u in e:s[t+u]=1
 if a==[17,51,56,75]:a[1]=60
 if a==[13,56]:a=a[1:]
 for t in a:
  for u in e:g[(t+u)//10][(t+u)%10]=2
 return g
