def p(g):# cross row of 2 and column of 8
 i=sum(g,[]).index;s=i(2)//6;c=i(8)%6;g=range(6)
 return[[y==s and 2<<(x==c) or 8*(x==c) for x in g]for y in g]
