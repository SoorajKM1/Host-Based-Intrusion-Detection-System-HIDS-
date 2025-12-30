# File Integrity Monitoring (FIM) System

import hashlib
import os
import time
from alert import log_alert

files_to_monitor = ["testfile.txt"]
baseline = {}

def calculate_hash(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'rb') as f:
            return hashlib.sha256(f.read()).hexdigest()
    return None

# creating a baseline:
print("Creating baseline...")
for f in files_to_monitor:
    baseline[f] = calculate_hash(f)
    print(f"Baseline created: {baseline}")

# monitoring for changes:
def start_fim():
    # creating a baseline on startup:
    print("[FIM] Creating baseline...")
    for f in files_to_monitor:
        baseline[f] = calculate_hash(f)
        print(f"[FIM] Baseline created for {f}: {baseline[f]}. Monitoring now for changes...")

    while True:
        time.sleep(5)  # Check every 5 seconds
        for f in files_to_monitor:
            current_hash = calculate_hash(f)
            if baseline[f] != current_hash:
                log_alert(f"FILE INTEGRITY ERROR: {f} has been modified! New Hash: {current_hash}")
                baseline[f] = current_hash  # Update baseline to new hash

if __name__ == "__main__":
    start_fim()