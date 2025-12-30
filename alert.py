#The Alert System
import datetime
import os
import requests
import json
import threading
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

discord_webhook_url = os.getenv("discord_webhook_url")

#accounting for missing webhook url
if not discord_webhook_url:
    print("[!] Warning: Discord webhook URL not found in environment variables.")


def send_discord_alert(message): # sends the message to discord in a background thread.

    data = {
        "content": "",
        "embeds": [
            {
                "title": "🚨 HIDS SECURITY ALERT",
                "description": message,
                "color": 16711680
                "timestamp": datetime.datetime.utcnow().isoformat()
            }
        ]
    }
    try:
        requests.post(discord_webhook_url, json=data, timeout=5)
    except Exception as e:
        print(f"[!] Failed to send Discord alert: {e}")

def log_alert(message): # Logs to file, prints to console, and sends to discord
    
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_msg = f"[{timestamp}] {message}"
    
    print(formatted_msg) # 1. Print to Console
    
    with open("hids_alerts.log", "a") as f: # 2. Log to File
        f.write(formatted_msg + "\n")
    
    # 3. Send to Discord using a seperate thread
    t = threading.Thread(target=send_discord_alert, args=(formatted_msg,))
    t.start()
