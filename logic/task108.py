def p(g):r=range(0,9,2);return[[max(g[i][j:j+2]+g[i+1][j:j+2])for j in r for _ in'0'*4]for i in r for _ in'0'*4]#2x2 max then 4x bigger
