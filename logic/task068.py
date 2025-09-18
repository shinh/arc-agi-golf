def p(g):# halo unique
    a=sum(g,[]);v=min(a,key=a.count);k=a.index(v);r=range(10);return[[(i*10+j==k)*v or 2*(2>i-k//10>-2<j-k%10<2)for j in r]for i in r]

