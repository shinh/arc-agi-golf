def create(rows, cols):
    return [[0 for _ in range(cols)] for _ in range(rows)]

def show(g):
    for r in g:
        a=[]
        for c in r:
            a.append(str(c))
        print("".join(a))