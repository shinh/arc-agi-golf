def p(j):
 # mark diagonals 1..4 around 2x2 block of 5s
 A=len(j)-1;c=len(j[0])-1
 for E in range(A):
  for k in range(c):
   if j[E][k]==j[E][k+1]==j[E+1][k]==j[E+1][k+1]==5:
    if E:
     if k:j[E-1][k-1]=1
     if k<c-1:j[E-1][k+2]=2
    if E<A-1:
     if k:j[E+2][k-1]=3
     if k<c-1:j[E+2][k+2]=4
 return j
