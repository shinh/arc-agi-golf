def p(g):
    a=sum(g,[]);k=a.index(min(a,key=a.count));r=range(10)
    return[[(i*10+j==k)*a[k] or 2*(2>i-k//10>-2<j-k%10<2)for j in r]for i in r]