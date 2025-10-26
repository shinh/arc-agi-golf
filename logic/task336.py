# fill interior via spins
p=lambda g,t=4:t and p([(f:=0)or[(c+(f==1>c)*8,f:=f+(c==5)*(d<4 or f))[0]for d,c in enumerate(r)]for r in zip(*g[::-1])],t-1)or g
