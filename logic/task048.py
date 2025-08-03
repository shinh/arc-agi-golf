def p(g):
 d=sum(r.count(8)-r.count(2)for r in g)%5
 return[[8*(d and d!=3)]]
