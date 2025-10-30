def p(g):a,b=[[(*x,1).index(1)+2for x in z]for z in(zip(*g),g)];e=enumerate;return[[v-v//4*(i in a or j in b)for j,v in e(r)]for i,r in e(g)]
