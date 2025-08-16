#2+ same
p=lambda g,E=enumerate:[[v*((r[j-1:j]+r[j+1:j+2]+[w[j]for w in g[i-1:i]+g[i+1:i+2]]).count(v)>1)for j,v in E(r)]for i,r in E(g)]
