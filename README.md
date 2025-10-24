# Streamlit Demo

This is a minimal Streamlit project.

Files
- `app.py` - the Streamlit app entry point.
- `requirements.txt` - Python dependencies (pinned).

Quick start (PowerShell)

1. Open a PowerShell terminal in the project folder:

```powershell
cd C:\Users\acer\streamlit-demo
```

2. Create a virtual environment (if you haven't already):

```powershell
python -m venv .venv
```

3. Activate the venv for this session (temporary bypass if necessary):

```powershell
Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process -Force
.\.venv\Scripts\Activate.ps1
```

(Or use CMD without changing execution policy)

```cmd
.venv\Scripts\activate.bat
```

4. Install dependencies:

```powershell
pip install -r requirements.txt
```

5. Run the app:

```powershell
streamlit run app.py
# or, without activation
.venv\Scripts\python.exe -m streamlit run app.py
```

6. Open the URL printed by Streamlit (usually http://localhost:8501).

Generating `requirements.txt` from a venv

```powershell
.venv\Scripts\python.exe -m pip freeze > requirements.txt
```

Notes & troubleshooting
- If you see a pip warning such as:
  `The script watchmedo.exe is installed in 'C:\Users\acer\AppData\Roaming\Python\Python314\Scripts' which is not on PATH.`
  you can add that directory to your user PATH so user-installed scripts are available system-wide.

  Example (PowerShell, sets user PATH):

```powershell
[Environment]::SetEnvironmentVariable("PATH", $env:PATH + ";C:\Users\acer\AppData\Roaming\Python\Python314\Scripts", "User")
```

- If PowerShell blocks activation scripts, use the Process-scope bypass above or run the CMD activator (`activate.bat`).
- To stop the running Streamlit server: press `Ctrl+C` in the terminal where it runs.

Security
- The Network URL (e.g. `http://192.168.0.124:8501`) exposes the app on your LAN. Only use it if you trust devices on your network and your firewall rules allow it.

Contact
- If you want I can add more example widgets, a small test, or CI instructions.
