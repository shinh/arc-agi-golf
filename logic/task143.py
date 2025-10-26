def p(g):
 t=sum(g,[]);P=[i for i in range(23)if t[i]*(i%10<3)];b=1
 while len({t[b+j]for j in P})^1|t.count(t[b+P[0]])-len(P):b+=1
 for j in P:t[b+j]=5
 return[*zip(*[iter(t)]*10)]
