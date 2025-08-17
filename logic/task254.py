def p(g):
 g=[[0]*len(B:=[sum(map(bool,c))for c in zip(*g)])for _ in g]# count nonzero per column then draw bars
 for v,n in(2,min({*B}-{0})),(1,max(B)):
  for r in g[-n:]:r[B.index(n)]=v
 return g

