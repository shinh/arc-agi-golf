def p(g):#move 5s toward 2 cluster
 t=sum(g,[]);y,x=divmod(t.index(2)-11,10);o=[[v&2 for v in r]for r in g]
 for i in range(100):
  if t[i]>4:o[min(y+3,max(y,i//10))][min(x+3,max(x,i%10))]=5
 return o
