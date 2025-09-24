def p(g):#
    s=sum(g,[]);t=sorted((s.count(i),s.index(i)%10,i)for i in{*s}-{0});m=t[-1][0];return[[c for a,_,c in t if a==m]]*m
