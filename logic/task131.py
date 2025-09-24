def p(g):
 #drop3sunder2add8
 if (w:=len(g[0]))>(h:=len(g)):return [*zip(*p([*zip(*g)]))]
 s=sum(map(list,g),[])
 a=s.index(2)//w;b=s.index(3)//w;s=h-s[::-1].index(3)//w
 return p(g[::-1])[::-1]if b<a else g[:a+1]+g[b:s]+[(8,)*w]+[(0,)*w]*(h-a+b-s-2)

