# stolen from: https://www.kaggle.com/code/kenkrige/chipping-skills-3-regex (comments)
import re
def p(i):
 r=re.sub(', ','',str(i+[*zip(*i)]));r+=r[::-1];i=int(max(r,key=r.count));l={0:(0,i)}
 for t in range(10):
  if(t!=i)*(e:=re.findall(f'{t}+',r)):d=len((re.findall(f'{t}{t}([^]){t}]+){t}',r)or[''])[0]);o=len(max(e))*((d>0)+1);l[o+d>>1]=d+1>>1,t
 return[[i*((d:=l[r[1]])[0]>r[0])or d[1]for t in range(-max(l),max(l)+1)if(r:=sorted((abs(t),abs(e))))]for e in range(-max(l),max(l)+1)]

# # 353
# # longest runs -> cross arms
# def p(g):
#  R=range;bg=max(g[0],key=g[0].count);t=g+[*zip(*g)];m=[];L=0
#  for c in R(10):
#   mx=0,
#   for r in t:
#    if c in r:a=r.index(c);b=len(r)-r[::-1].index(c);k=b-a;n1=next((i for i in R(k)if r[a+i]-c),k);n2=next((i for i in R(k)if r[b-1-i]-c),k);mx=max(mx,(k+abs(n1-n2),max(n1,n2)))
#   if mx[0]and c-bg:L=max(L,mx[0]);m+=[(c,*mx)]
#  o=[[bg]*L for _ in R(L)]
#  for c,n,q in m:
#   n+=n==2;y=L-n>>1
#   for _ in R(4):
#    for i in R(q):o[y][y+i]=o[y+i][y]=c
#    o=[*map(list,zip(*o[::-1]))]
#  return o
