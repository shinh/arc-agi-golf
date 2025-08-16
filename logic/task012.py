# expand cross pattern into larger diamond with cross arms
def p(g,r=range(-2,3),E=enumerate):
    G=[*map(list,g)]
    [G[i+D].__setitem__(j+F,R[j-1] if D*D-F*F else x)for i,R in E(g)for j,x in E(R)if x and R[j-1]*R[j+1]for D in r for F in r if(D*D-F*F)*D*F==0]
    return G

