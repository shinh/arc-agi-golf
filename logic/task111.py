def p(g):
 # flatten index and crop
 i=sum(g,[]).index(5);w=len(g[0])
 return[g[i//w+j][i%w-1:i%w+2]for j in(1,2,3)]

