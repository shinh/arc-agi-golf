def p(g):
 # choose pattern based on highest color in grid
 a=[0,5,0];h=[5]*3
 return{2:[h,a,a],1:[a,h,a],3:[[0,0,5]]*2+[h]}[max(sum(g,[]))]
