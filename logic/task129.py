# fill 3x3 with dominant color
p=lambda g:[[max(g:=sum(g,[]),key=g.count)]*3]*3
