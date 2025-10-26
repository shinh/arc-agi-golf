def p(a):
    e=enumerate;s=[i for i,r in e(a)if any(r)];r=s[1];v=max(a[r]);return[[v*(max(abs(i-r),abs(j-a[r].index(v)))%(r-s[0])<1)for(j,_)in e(R)]for(i,R)in e(a)]