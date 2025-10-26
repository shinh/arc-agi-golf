def p(o):
 for i,j in[(i,j)for i in range(17)for j in range(17)if not(o[i][j]|o[i][j+1]|o[i+1][j]|o[i+1][j+1])and(not j or o[i][j-1]|o[i+1][j-1])and(j>15 or o[i][j+2]|o[i+1][j+2])]:o[i][j:j+2]=o[i+1][j:j+2]=2,2
 for i,j in[(i,j)for i in range(17)for j in range(17)if not(o[i][j]|o[i][j+1]|o[i+1][j]|o[i+1][j+1])and(not i or o[i-1][j]|o[i-1][j+1])and(i>15 or o[i+2][j]|o[i+2][j+1])]:o[i][j:j+2]=o[i+1][j:j+2]=2,2
 return o