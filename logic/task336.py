# spin fill
p=lambda g,t=4:t and p([(f:=0)or[c+8*((f:=f+(c==5)*(f|(4>d)))&1>c) for d,c in enumerate(r)]for r in zip(*g[::-1])],t-1)or g
