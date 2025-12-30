# 🛡️ Python Host-Based Intrusion Detection System (HIDS)

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python)
![Platform](https://img.shields.io/badge/Platform-Linux-orange?style=flat&logo=linux)
![Security](https://img.shields.io/badge/Type-Cybersecurity-red)

## 📌 Project Overview
A lightweight, multi-threaded **Host-Based Intrusion Detection System (HIDS)** built from scratch in Python. This tool monitors Linux environments for unauthorized file modifications and suspicious authentication attempts in real-time.

It acts as a custom security agent, combining **File Integrity Monitoring (FIM)** with **Log Analysis** to detect potential intrusions. The system features an integrated alerting engine that pushes real-time security telemetry to a **Discord Webhook**, enabling remote monitoring and rapid incident response.

## 🚀 Key Features
* **File Integrity Monitoring (FIM):** Uses **SHA-256 hashing** to create digital baselines of critical files. Detects and alerts on unauthorized changes instantly.
* **SSH Brute-Force Detection:** Monitors `/var/log/auth.log` using **Regex pattern matching** to identify repeated failed login attempts.
* **Real-Time Cloud Alerting:** Integrated **Discord API** to send instant push notifications to a mobile device/SOC channel.
* **Multi-Threaded Architecture:** Uses Python `threading` (daemon threads) to run multiple detection modules concurrently without blocking.
* **Secure Configuration:** Implements environment variable management (`.env`) to secure sensitive API credentials.


The system is composed of three modular components:
1.  **`main.py`:** The orchestration engine that initializes parallel threads for detection modules.
2.  **`fim.py`:** The integrity sensor that compares current file hashes against the known-good baseline.
3.  **`log_monitor.py`:** The log watchdog that "tails" system logs to catch attack signatures.
4.  **`alert.py`:** A centralized alerting service that handles logging to disk and pushing payloads to Discord.

## 💻 Tech Stack
* **Language:** Python 3.x
* **OS:** Linux (Ubuntu Server 24.04/22.04)
* **Libraries:** `hashlib`, `re`, `threading`, `requests`, `python-dotenv`
* **Tools:** VirtualBox, SSH, VS Code

## ⚙️ Installation & Setup
Follow the steps below to install, configure, and run the HIDS on your Linux machine.

## 1. System Update
Before installing dependencies, ensure your system packages are up to date to avoid conflicts:

```bash

sudo apt update && sudo apt upgrade -y
```

## 2. Clone the Repository
Clone the project repository and navigate into the project directory:

```bash

git clone https://github.com/YOUR_USERNAME/Host-Based-Intrusion-Detection-System-HIDS-.git
cd Host-Based-Intrusion-Detection-System-HIDS-
```

## 3. Install Python & Dependencies
Ensure Python 3 and pip are installed on your system:

```bash

sudo apt install python3 python3-pip -y
```

## Install the required Python libraries using pip:

```bash

pip3 install requests python-dotenv
```

## 🔐 Configuration (Secrets Management)
This project uses environment variables to securely store sensitive information, such as the Discord Webhook URL, without hardcoding them into the script.

Create the .env File
In the project root directory, create a new file named .env:

```bash

nano .env
```

* Add your Discord Webhook URL to the file in the following format:
```bash
DISCORD_WEBHOOK_URL=https://discord.com/api/webhooks/YOUR_ID/YOUR_TOKEN
```
* Note: Save your changes by pressing Ctrl + O, then Enter. Exit the editor by pressing Ctrl + X.


## 🚀 Running the HIDS
The Log Monitor module needs to read /var/log/auth.log, which is a protected system file. Therefore, you must run the script with sudo privileges.

```bash

sudo python3 main.py
```

## ✅ Verification
Once the script is running, check for the following:

* Terminal Output: You should see messages confirming that the FIM and Log Monitor threads have started successfully.
* Discord Alert: Check your Discord channel; the system is designed to send a "System Online" notification immediately upon startup.
