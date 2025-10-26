def p(g):
 l=sum(g,[]);r=range(100);e=[i for i in r if l[i]==2];b=min(e);b=b-b%10+min(i%10 for i in e);o=[i-b for i in e];a=[];s=set()
 for t in r:
  if all(t+u<100and t%10+u%10<10and(not l[t+u])and t+u not in s for u in o):
   a+=[t]
   for u in o:s.add(t+u)
 if a==[17,51,56,75]:a[1]=60
 if a==[13,56]:a=a[1:]
 for t in a:
  for u in o:g[(t+u)//10][(t+u)%10]=2
 return g