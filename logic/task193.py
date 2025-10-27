#2+ same
p=lambda g,E=enumerate:[[v*((*r[j-(j>0):j+2],*[*zip(*g[i-(i>0):i+2])][j]).count(v)>3)for j,v in E(r)]for i,r in E(g)]
