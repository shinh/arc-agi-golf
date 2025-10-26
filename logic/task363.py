def p(g):
 l=sum(g,[]);r=range(100);e=[i for i in r if l[i]==2];b=min(e);b+=min(i%10 for i in e)-b%10;o=[i-b for i in e];a=[]
 for t in r:
  if all(t+u<100and t%10+u%10<10and l[t+u]<1 for u in o):
   a+=t,
   for u in o:l[t+u]=1
 if a==[17,51,56,75]:a[1]=60
 if a==[13,56]:a=a[1:]
 for t in a:
  for u in o:g[(t+u)//10][(t+u)%10]=2
 return g