def p(g):
    r=[[max(g[2*i][2*j:2*j+2]+g[2*i+1][2*j:2*j+2])for j in range(5)]for i in range(5)]
    return[[c for c in row for _ in range(4)]for row in r for _ in range(4)]
