import argparse
import os

import code_golf_utils


def submit(task_id):
    print("Submitting task", task_id)

    try:
        core = open("logic/core.py").read()
        logic = open(f"logic/task{task_id:03d}.py").read()
        code = core + "\n" + logic
        task_path = f"submissions/task{task_id:03d}.py"
        open(task_path, "w").write(code)

        examples = code_golf_utils.load_examples(int(task_id))
        if code_golf_utils.verify_program(task_id, examples, task_path):
            open(f"reports/task{task_id:03d}.txt", "w").write(str(2500 - len(code)))
        else:
            open(f"reports/task{task_id:03d}.txt", "w").write("FAIL")
    except:
        open(f"reports/task{task_id:03d}.txt", "w").write("ERROR")


def main():
    parser = argparse.ArgumentParser(description="Submit code golf.")
    parser.add_argument("task_id")
    args = parser.parse_args()

    if args.task_id == "all":
        for task_id in range(1, 401):
            submit(task_id)
    else:
        submit(int(args.task_id))


if __name__ == "__main__":
    main()
