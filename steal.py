import glob
import os
import shutil
import subprocess
import sys


def check_score(task_id, code_dir):
    result = subprocess.run(
        [sys.executable, "submit.py", str(task_id), "--code_dir", code_dir],
        capture_output=True,
    )
    if result.returncode != 0:
        return None
    return int(result.stdout.split()[-1])


def main():
    new_dir = sys.argv[1]
    for py in sorted(glob.glob(os.path.join(new_dir, "task*.py"))):
        task_id = int(os.path.basename(py)[4:7])
        base_score = check_score(task_id, "logic")
        if base_score is None:
            raise RuntimeError(f"Baseline is broken for task {task_id}")

        new_score = check_score(task_id, new_dir)
        if new_score is None:
            print(f"Task {task_id:03d}: {py} is broken", flush=True)
            continue

        print(f"Task {task_id:03d}: {base_score} => {new_score}", flush=True)

        if new_score > base_score:
            shutil.copy(py, os.path.join("logic", os.path.basename(py)))


if __name__ == "__main__":
    main()
