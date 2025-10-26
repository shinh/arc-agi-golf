def p(g):
 A=sum(g,[]);G=sum({*A})-2
 while 2in A:
  D=A.index(2);B,C=D//9,D%9;E=A[D-9]>0 or-1;F=A[D-1]>0 or-1
  while 9>B>-1<C<9:
   g[B+(9>B+E>=0)*E][C]=g[B][C+(9>C+F>=0)*F]=g[B][C]=G;B+=E;C+=F
  A[D]=G
 return g