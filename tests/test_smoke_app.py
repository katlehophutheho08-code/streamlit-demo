import subprocess
import sys


def test_app_imports_in_new_process():
    """Smoke test: import the `app` module in a fresh Python process.

    This verifies the application module can be imported without raising
    in a clean interpreter (closer to 'starting' the app without fully
    launching the Streamlit server).
    """
    cmd = [sys.executable, '-c', 'import importlib; importlib.import_module("app")']
    # Run the command; if import fails this will return non-zero or raise
    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=10)
    assert res.returncode == 0, f"Import failed: {res.stderr.decode()!r}"
