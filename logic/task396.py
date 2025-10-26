def p(a):
 h,w=len(a),len(a[0])
 A=max((((D:=next((j for j in range(y,h)if a[j][x]!=f),h))-y)*((E:=next((i for i in range(x,w)if a[y][i]!=f),w))-x),f,y,x,D,E)for y in range(h)for x in range(w)if(f:=a[y][x]))
 g=sum({*sum(a,[])})-A[1]
 return[[[g,v][v!=A[1]]for v in r[A[3]:A[5]]]for r in a[A[2]:A[4]]]