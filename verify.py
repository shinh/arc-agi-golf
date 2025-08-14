import argparse
import sys

import code_golf_utils

try:
    import matplotlib.pyplot as plt
except Exception:  # pragma: no cover - fallback if matplotlib unavailable
    class _P:
        def __getattr__(self, _):
            return lambda *a, **k: None
    plt = _P()

def main():
    parser = argparse.ArgumentParser(description="Show code golf examples.")
    parser.add_argument("task_id")
    parser.add_argument("--code_dir")
    parser.add_argument("--debug", action="store_true", help="Enable debug mode")
    args = parser.parse_args()

    code_dir = args.code_dir or "logic"

    task_id = "%03d" % int(args.task_id)

    code = open("logic/core.py").read()
    code += "\n"

    task_code = open(f"{code_dir}/task{task_id}.py").read()

    if args.debug or "show" in task_code:
        code += open("logic/debug.py").read()
        code += "\n"

    code += task_code
    open("task.py", "w").write(code)

    examples = code_golf_utils.load_examples(int(task_id))
    if not code_golf_utils.verify_program(int(task_id), examples):
        plt.savefig("error.png")
        print("FAILED!!")
        sys.exit(1)


if __name__ == "__main__":
    main()
