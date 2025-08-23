# 4->6 every 3rd cell
p=lambda g:[[v+2*(v==4)*(i%3<1)for i,v in enumerate(r)]for r in g]

