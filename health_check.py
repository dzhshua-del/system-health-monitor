import os
import platform
import shutil
import subprocess
from datetime import datetime

def get_disk_usage():
    total, used, free = shutil.disk_usage("/")
    percent_used = (used / total) * 100
    return f"{used // (2**30)}GB / {total // (2**30)}GB ({percent_used:.1f}%)"

def check_git_identity():
    try:
        email = subprocess.check_output(["git", "config", "user.email"], text=True).strip()
        name = subprocess.check_output(["git", "config", "user.name"], text=True).strip()
        return f"{name} <{email}>"
    except subprocess.CalledProcessError:
        return "Git identity not configured"

def run_health_check():
    print("=" * 45)
    print(f"SYSTEM & DEV HEALTH REPORT | {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print("=" * 45)
    print(f"OS Platform   : {platform.system()} {platform.release()}")
    print(f"Python Version: {platform.python_version()}")
    print(f"CPU Cores     : {os.cpu_count()}")
    print(f"Disk Usage    : {get_disk_usage()}")
    print(f"Git User      : {check_git_identity()}")
    print("=" * 45)

if __name__ == "__main__":
    run_health_check()