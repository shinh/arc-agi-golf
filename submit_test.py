import os
import sys

import submit


def test_run_range(monkeypatch, capsys, tmp_path):
    """submit.py start-end runs the specified range and reports total score."""

    calls = []

    def fake_submit(task_id, args, verbose):
        calls.append(task_id)
        os.makedirs("reports", exist_ok=True)
        with open(f"reports/task{task_id:03d}.txt", "w") as f:
            f.write("1")
        print(f"Task {task_id:03d}: 1")
        return True

    monkeypatch.setattr(submit, "submit", fake_submit)
    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(sys, "argv", ["submit.py", "3-7"])
    submit.main()
    out = capsys.readouterr().out

    assert calls == [3, 4, 5, 6, 7]
    assert "Total score: 5" in out
