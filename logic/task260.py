# extend diagonal endpoints while clearing intruders
p=lambda g,e=enumerate:(lambda a,b,c,d:[[(x%5 and x,c)[(a<d)*(i-j==a-2)+(b>d)*(i-j==b+2)]for j,x in e(r)]for i,r in e(g)])(min(i-j for i,r in e(g)for j,x in e(r)if x==5),max(i-j for i,r in e(g)for j,x in e(r)if x==5),*next((v,i-j)for i,r in e(g)for j,v in e(r)if v%5))
