# expand pattern marked by 2
p=lambda g,X=range(9):[[g[r//3][c//3]//2*g[r%3][c%3]for c in X]for r in X]
