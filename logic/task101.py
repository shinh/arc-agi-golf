def p(A):
 n=len(A);m=len(A[0]);M=[];G=[]
 def o(i,j):
  M.append((i,j))
  A[i][j]==2 and G.append((i,j));A[i][j]=0
  i and A[i-1][j] and o(i-1,j)
  i+1<n and A[i+1][j] and o(i+1,j)
  j and A[i][j-1] and o(i,j-1)
  j+1<m and A[i][j+1] and o(i,j+1)
 for i in range(n):
  for j in range(m):
   A[i][j]==1 and o(i,j)
 P,Q=min(G)
 for i in range(n):
  for j in range(m):
   if A[i][j]==2:
    a=1
    while i+a<n and A[i+a][j]==2:a+=1
    b=1
    while j+b<m and A[i][j+b]==2:b+=1
    s=min(a,b)
    for r,t in M:
     for x in range(s):
      for y in range(s):
       u=i+(r-P)*s+x;v=j+(t-Q)*s+y
       if 0<=u<n and 0<=v<m:
        A[u][v]==2 and G.append((u,v))
        A[u][v]=1
 for i,j in M: A[i][j]=1
 for i,j in G: A[i][j]=2
 return A