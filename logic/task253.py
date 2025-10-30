def p(j):#L
 a,b,c,d=map(max,zip(*((a*(a==b==c),a*(a==b==d),a*(a==c==d),d*(b==c==d))for r,s in zip(j,j[1:])for a,b,c,d in zip(r,s,r[1:],s[1:]))));return(a,a,c,c),(a,0,0,c),(b,0,0,d),(b,b,d,d)
