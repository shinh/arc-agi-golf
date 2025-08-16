# map color count to row/diag pattern
p=lambda g:[[5*(y==[0,x,2-x][len({*sum(g,[])})-1])for x in(0,1,2)]for y in(0,1,2)]
