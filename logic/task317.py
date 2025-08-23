def p(E):#1 near 5
 r=range(len(E));return[[any(5 in R[j-(j>0):j+2]for R in E[i-(i>0):i+2])for j in r]for i in r]
