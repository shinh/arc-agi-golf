# recolor rectangular loops
p=lambda g,t=0:g*(t-143)or p([[[c,[2,3,0][q:=t//48]][c==q and n%(5-q*2)==(q<1)*2]for c,n in zip(r,[*r[1:],2])]for r in zip(*g[::-1])],t+1)
