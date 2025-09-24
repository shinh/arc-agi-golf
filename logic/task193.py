#2+ same
p=lambda g,E=enumerate:[[v*((r[j-(j>0):j+2]+[w[j]for w in g[i-(i>0):i+2]]).count(v)>3)for j,v in E(r)]for i,r in E(g)]
