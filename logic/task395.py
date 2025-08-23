# compare top rows with those 3 below
p=lambda g:[[(a+b<1)*2for a,b in zip(*g[y::3])]for y in(0,1,2)]

