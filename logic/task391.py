# colors ranked 3-5 by frequency
p=lambda g:(*zip(sorted({*(a:=sum(g,[]))},key=a.count)[-3:-6:-1]),)

