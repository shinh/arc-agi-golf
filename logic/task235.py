# decode 3-bit color id complements
p=lambda g:[[9-(g[2][x-1]+2*g[2][x]+4*g[1][x])//5]*3for x in(1,6,11)]

