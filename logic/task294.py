# rotate flood-fill to erode 5-pixels
p=lambda g:(f:=lambda m,n=4:n and f([[a*b//5 for a,b in zip(r,r[1:]+(0,))]for r in zip(*m[::-1])],n-1)or m, [[c-3*(d>0) for c,d in zip(r,t)]for r,t in zip(g,f(g))])[1]
