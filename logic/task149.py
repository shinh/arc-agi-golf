# count 6s
t=0,4,8
p=lambda g:[[sum(r[j:j+4].count(6)for r in g[i:i+4])>1for j in t]for i in t]
