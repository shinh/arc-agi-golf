p=lambda g:[[sorted(sum(zip(*g[i:i+3]),())[j:j+9])[4]for j in(0,9,18)]for i in(0,3,6)]
