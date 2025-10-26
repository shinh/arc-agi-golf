def p(g):
 t=sum(g,[]);P=[i for i in range(23)if i%10<3 and t[i]]
 b=next(i for i in range(1,78)if len({t[i+j]for j in P})<2 and t.count(t[i+P[0]])==len(P))
 for j in P:t[b+j]=5
 return[*zip(*[iter(t)]*10)]