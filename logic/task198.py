# rotate grid and paint
# 147
p=lambda g,n=23:-n*g or p([[[a,3+(b>0<3!=b)*(b in c+[4])][a in(0,3)]for a,b,*c in zip(r,[*r[1:],3],r[2:]+(3,3),[3,*r])]for r in zip(*g[::-1])],n-1)
