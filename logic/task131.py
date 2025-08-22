def p(g):
 #drop3sunder2add8
 w=len(g[0])
 if w>len(g):return [*zip(*p([*zip(*g)]))]
 s=sum(map(list,g),[])
 a=s.index(2)//w;b=s.index(3)//w;s=len(g)-s[::-1].index(3)//w
 if b<a:return p(g[::-1])[::-1]
 return g[:a+1]+g[b:s]+[(8,)*w]+[(0,)*w]*(len(g)-a+b-s-2)

