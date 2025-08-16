#!/usr/bin/env python3

import glob
import os

import sota

ours = []
for py in sorted(glob.glob("submissions/*.py")):
    ours.append(os.path.getsize(py))

assert len(ours) == 400, str(len(ours))

theirs = sota.read_sota()

for i in range(400):
    o = ours[i]
    t = theirs[i]
    prefix = f"Task{i+1:03d}"
    if o < t:
        print(prefix, f"We win! {o} vs {t}")
    elif o == t:
        print(prefix, f"Tie. {o}")
    else:
        print(prefix, f"{o-t} bytes from theirs: {o} vs {t}")
