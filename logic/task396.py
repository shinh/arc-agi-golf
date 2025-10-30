def p(a):# crop&paint
 m,c,y,x,d,e=max(((D:=next((i for i,R in enumerate(a[Y:])if R[X]^f),len(a)-Y))*(E:=next((i for i,v in enumerate(r[X:])if v^f),len(r)-X)),f,Y,X,D,E)for Y,r in enumerate(a)for X,f in enumerate(r)if f);t=sum({*sum(a,[])})-c;return[[(v,t)[v==c]for v in r[x:x+e]]for r in a[y:y+d]]
