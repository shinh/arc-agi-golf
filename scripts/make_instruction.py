#!/usr/bin/env python3

import argparse
import glob
import json
import os

import sota


def read_ours():
    ours = []
    for code, o in zip(sorted(glob.glob("logic/*.py")), sorted(glob.glob("ours/*.txt"))):
        ours.append((2500 - int(open(o).read()), open(code).read()))
    return ours


def main():
    parser = argparse.ArgumentParser(description="Make an instruction for AI.")
    parser.add_argument("task_id")
    parser.add_argument("--select-important", action="store_true", help="Select an important task.")
    args = parser.parse_args()

    ours = read_ours()
    theirs = sota.read_sota()

    task_id = args.task_id

    if args.select_important:
        diffs = []
        for i, ((our, _), their) in enumerate(zip(ours, theirs)):
            diff = their - our
            diffs.append((diff, i + 1))
        diffs.sort()
        # +1 for task157
        task_id = "%03d" % diffs[int(task_id) + 1][1]
        print(f"Selected important task {task_id}")
    else:
        task_id = "%03d" % int(task_id)

    categories = json.load(open("scripts/categories.json"))

    categroy = set(categories[task_id])

    similar_tasks = []
    for t, cs in categories.items():
        if t == task_id:
            continue
        mutual_cats = categroy and set(cs)
        if mutual_cats:
            ti = int(t) - 1
            ratio = theirs[ti] / ours[ti][0]
            similar_tasks.append((ratio, ours[ti][1], list(mutual_cats), t))

    similar_tasks.sort()
    # print(similar_tasks)

    our_score = 2500 - ours[int(task_id) - 1][0]
    known_best = min(ours[int(task_id) - 1][0], theirs[int(task_id) - 1])
    known_best_score = 2500 - known_best

    title = f"Your task is to **rewrite `logic/task{task_id}.py` into a fully code-golfed solution**"

    print(r"""{title}

### Rules
    - The rewritten code must pass **all official test cases** (checked with `python3 verify.py <task_id>`).
    - Do **not** delete comments or rename symbols. They will be minified automatically later. Add comments to describe the approach.
    - When code is long (e.g., >200B), you may duplicate code or write long expressions: final submission will be compressed by zlib.

### Workflow
    1. Record the **initial score**:

    python3 submit.py <task_id> | tail -n 1

    2. Rewrite the code to minimize size (golf as much as possible).
    3. Verify correctness:

    python3 verify.py <task_id>

    4. Record the **final score** the same way as step 1.
    5. Report both first and final scores.

Repeat the rewrite-and-submit process multiple times, reporting the score after each attempt, until no further reduction is achieved. Among all attempts, select the best-performing version (the one with the highest score) and commit that as the final solution.

Known best score is {known_best_score}.

### References

This task's categories are {categories}. Here is the list of code similar to this task:

""".format(title=title, categories=categories[task_id], known_best_score=known_best_score, our_score=our_score))

    for ratio, code, cats, tid in similar_tasks[:5]:
        print(r"""task{tid}: categories={cats}

{code}
""".format(code=code.strip(), cats=cats, tid=tid))


if __name__ == "__main__":
    main()
