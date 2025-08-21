# pair columns 0..2 with 4..6, output 2 if both cells nonzero
p=lambda g:[[r[i]*r[i+4]and 2 for i in(0,1,2)]for r in g]

