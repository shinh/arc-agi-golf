def p(E):#1 near 5
 r=range(len(E));return[[any(5 in R[j and j-1:j+2] for R in E[i and i-1:i+2])for j in r]for i in r]
