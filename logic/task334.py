# choose pattern based on highest color in grid
a=0,5,0;h=5,5,5;b=0,0,5
p=lambda g:[0,(a,h,a),(h,a,a),(b,b,h)][max(sum(g,[]))]
