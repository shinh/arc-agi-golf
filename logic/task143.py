def p(g):
 t=sum(g,[]);P=[i for i in range(23)if t[i]>0>i%10-3];b=1
 while len({t[b+j]for j in P})^1|len(P)^t.count(t[b+P[0]]):b+=1
 for j in P:g[(b+j)//10][(b+j)%10]=5
 return g
