from re import sub
p=lambda g,t=7:-t*g or p(eval(sub(r"0(?=(.{34}(.{35}){0,9})8.{34}8|(.{34}(.{35}){0,9})3(.{34})2)","3",str([*zip(*g[::(-1)**(t&1)])]))),t-1)
