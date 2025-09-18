# count 2x2 blocks of color 1
p=lambda g:[(sum({*y}=={1}for a,b in zip(g,g[1:])for y in zip(a,b,a[1:],b[1:]))*[1]+5*[0])[:5]]

