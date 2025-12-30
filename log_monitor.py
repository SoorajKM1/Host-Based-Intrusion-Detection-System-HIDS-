# Log Monitoring System

# We know that Ubuntu saves every log in attempt and it is saved at: /var/log/auth.log
import time
import os 
from alert import log_alert
LOG_FILE_PATH = "/var/log/auth.log"

def follow(file_path): # Generator function to follow the log file
    file_path.seek(0,2) # Move to the end of the file
    while True:
        line = file_path.readline()
        if not line:
            time.sleep(0.1) # Sleep for a while before checking for new lines
            continue
        yield line

def start_log_monitor():
    print(f"Monitoring {LOG_FILE_PATH} for failed login attempts...")
    try:
        with open(LOG_FILE_PATH, "r") as log_file:
            log_lines = follow(log_file)
            for line in log_lines:
                if "Failed password" in line:
                    log_alert(f"SSH BRUTE FORCE DETECTED: {line.strip()}")
    except FileNotFoundError: #accounting for file not found error
        print(f"Error: Log file {LOG_FILE_PATH} not found.")
    except PermissionError: #accounting for permission issues as well
        print(f"Error: Permission denied when trying to read {LOG_FILE_PATH}.")

if __name__ == "__main__":
    start_log_monitor()