def p(j):r,c=divmod(sum(j,[]).index(2),5);return[[(i+r)%2*(abs(k-c)==1)*(3,6,8,7)[k>c::2][i>r]for k in range(5)]for i in(0,1,2)]
