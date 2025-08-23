# crop largest border of the most common color and recolor to rarest
def p(g):
 s=[v for v in sum(g,[])if v];a=max(s,key=s.count);b=min(s,key=s.count);H=len(g);W=len(g[0])
 _,y,x,h,w=max((h*w,y,x,h,w)for y in range(H)for x in range(W)for h in range(2,-~H-y)for w in range(2,-~W-x)if all(i*j*(h+~i)*(w+~j)or g[y+i][x+j]==a for i in range(h)for j in range(w)))
 return[[[b,v][v!=a]for v in r[x:x+w]]for r in g[y:y+h]]
