p=lambda g:(n:=len({*sum(g,[0])})-1,sum([[sum([[x]*n for x in r],[])]*n for r in g],[]))[1]#scale grid by number of colors
