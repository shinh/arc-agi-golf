def p(g):
 while 2in(A:=sum(g,[])):
  D=A.index(2);B=D//9;C=D%9;E,F=A[D-9]>0 or-1,A[D-1]>0 or-1
  while 9>B>-1<C<9:
   g[B][C]=g[B+(9>B+E>=0)*E][C]=g[B][C+(9>C+F>=0)*F]=sum({*A})-2;B+=E;C+=F
 return g
