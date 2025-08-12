# flood fill from first 2 block through 8s to other 2
def p(g):
 R=range;h=len(g);w=len(g[0]);s=sum(g,[]);i=s.index(2);v={(i//w+d//2,i%w+d%2)for d in R(4)}
 f=lambda x,y:any(-1<a<h and -1<b<w and(a,b)not in v and(g[a][b]==2 or g[a][b]==8 and(v.add((a,b))or f(a,b)))for a in R(x-1,x+2)for b in R(y-1,y+2))
 return[[8*any(f(*k)for k in tuple(v))]]
