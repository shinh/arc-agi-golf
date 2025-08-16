def p(g):#ignore0
 return[[max(g:=sum(g,[]),key=lambda x:x and g.count(x))]*2]*2
