def p(j):
 #max 2s
 E=-1
 for k,r in enumerate(j):
  for W,v in enumerate(r):
   if v and((k and j[k-1][W])|(W and r[W-1]))<1:
    l=J=1
    while r[W+l:][:1]>[0]:l+=1
    while j[k+J:]and j[k+J][W]:J+=1
    a=[C[W:W+l]for C in j[k:k+J]]
    if(C:=sum(z.count(2)for z in a))>E:E=C;e=a
 return e
