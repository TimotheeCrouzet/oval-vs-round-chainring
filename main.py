import subprocess
import sys

def main():
    cmd = ["uv", "run", "streamlit", "run", "dashboard/Simulation.py"]
    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as exc:
        sys.stderr.write(f"Command failed ({exc.returncode}): {' '.join(cmd)}\n")
        sys.exit(exc.returncode)

if __name__ == "__main__":
    main()
