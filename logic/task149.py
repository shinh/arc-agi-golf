def p(g):# count 6s
 R=range(0,9,4);return[[sum(r[j:j+4].count(6)for r in g[i:i+4])>1for j in R]for i in R]
