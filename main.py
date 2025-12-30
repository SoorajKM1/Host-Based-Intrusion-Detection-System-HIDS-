# Main Block (we combine both the FIM and log monitoring systems here)

import threading
import time
from fim import start_fim
from log_monitor import start_log_monitor 

if __name__ == "__main__":
    print(" HIDS BOOTING UP... ")
    print(" Note: Press Ctrl + C to exit the service at any time. ")

    # creating threads for both FIM and log monitoring
    fim_thread = threading.Thread(target=start_fim)
    log_monitor_thread = threading.Thread(target=start_log_monitor)

   
    fim_thread.daemon = True  # Using daemon here as it ensures they die when the main program dies
    log_monitor_thread.daemon = True

    # 3. Start threads
    fim_thread.start()
    log_monitor_thread.start()

    # keeping the main thread alive
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print(" HIDS SHUTTING DOWN... THANKS FOR USING OUR SERVICE! ")