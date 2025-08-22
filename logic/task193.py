#2+ same
p=lambda g,E=enumerate:[[v*((r[j-1:j]+r[j:j+2]+[w[j]for w in g[i:i+2]+g[i-1:i]]).count(v)>3)for j,v in E(r)]for i,r in E(g)]
