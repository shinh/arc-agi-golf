# count 6s
p=lambda g:[[sum(r[j:j+4].count(6)for r in g[i:i+4])>1 for j in(0,4,8)]for i in(0,4,8)]
