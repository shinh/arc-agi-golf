def p(g):
 B=[sum(map(bool,c))for c in zip(*g)];g=[[0]*len(B)for _ in g]# count nonzero cells per column and draw bars
 for v,n in((2,min({*B}-{0})),(1,max(B))):
  i=B.index(n)
  for r in g[-n:]:r[i]=v
 return g

