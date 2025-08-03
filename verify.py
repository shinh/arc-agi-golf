import argparse
import code_golf_utils


def main():
    parser = argparse.ArgumentParser(description="Show code golf examples.")
    parser.add_argument("task_id")
    args = parser.parse_args()

    task_id = "%03d" % int(args.task_id)

    code = open("logic/core.py").read()
    code += "\n"
    code += open(f"logic/task{task_id}.py").read()
    open("task.py", "w").write(code)

    examples = code_golf_utils.load_examples(int(task_id))
    code_golf_utils.verify_program(int(task_id), examples)


if __name__ == "__main__":
    main()
