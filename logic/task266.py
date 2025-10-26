def p(j):
 r,c=divmod(sum(j,[]).index(2),5)
 return[[(i%2^r%2)*(abs(k-c)==1)*[[3,8],[6,7]][k>c][i>r]for k in range(5)]for i in range(3)]