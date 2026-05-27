# MARK II 
Mark-2 is a Python Based keylogger project which scans for key strokes in real time but this is made entirely ethical it only starts 
logging when user presses start logging from the menu options and stops when pressed stop logging  , I used 
UI implementation for better experience and demo.

The system captures keyboard activity using OS-level event listeners, stores the logs locally in visible text files, and analyzes the collected data to detect suspicious behavior patterns. 
The project focuses on helping students understand how attackers misuse keylogging techniques and how cybersecurity professionals detect such activities.


# File architecture 
```
MARK-2
|
|__ __pycache__
|__ logs
|   |___ latest_log.txt
|   |___ log_2025-11-21_15-34-16.txt
|   |___ log_2025-11-27_15-37-01.txt
|
|__ reports
|   |___ analysis_report.txt
|
|__ analyzer.py
|__ gui.py
|__ logger.py
|__ main.py
|__ mark2 likhith (REPORT).pdf
```
#Tech stack used
This project is mainly Based on Python Programming Language using 

Python ------	Core programming language
pynput ------	Keyboard event listener
datetime ------	Timestamp generation
os ------	File and folder handling
Text Files ------	Local log storage


# MODULES
1. Logger Module
The Logger module captures keystrokes using Python’s system-level event listeners. 
Every key press is recorded and stored inside timestamped log files. 
Special keys are converted into readable text format for easier analysis.

Responsibilities:
Capture keyboard events
Record timestamps
Store logs locally
Handle special keys
Run continuously until stopped

2. Analyzer Module
The Analyzer module processes the generated log files and checks for suspicious behavior patterns. 
It identifies repeated sequences, abnormal typing speed, unusual backspace usage, and repetitive entries.

Responsibilities:
Read generated logs
Detect suspicious patterns
Analyze typing behavior
Generate readable summaries
Highlight anomalies


3. gui.py
The gui.py file is responsible for creating a User Interface that displays 3 options for user to select

Responsibilities:
creating an UI
Display the title and options

4. main.py
This file is responsible for combining all those files and make a one file that gives output by importing
functions from all other modules or files


# Workflow

1. Start the Python application
2. Initialize the keyboard listener
3. Capture keystrokes in real time
4. Store logs inside local files
5. Run analyzer on generated logs
6. Detect abnormal patterns
7. Generate analysis summary


# Installation

Step 1: Install Python
Download and install Python from: 
  https://www.python.org/downloads/

Step 2: Install Required Library
Open terminal or command prompt and run:
  pip install pynput

Step 3: Run the Logger
  python logger.py
  
Step 4: Run the Analyzer
  python analyzer.py
  
# Example Output:
[12:45:10] H
[12:45:11] e
[12:45:11] l
[12:45:11] l
[12:45:12] o
[12:45:13] Key.space
[12:45:14] W
[12:45:14] o
[12:45:15] r
[12:45:15] l
[12:45:15] d

# Disclaimer
This project is intended only for ethical and educational purposes. 
Any misuse of this software against unauthorized systems or users is strictly discouraged. 
The developer is not responsible for unethical usage.

# Author
Developer : K. Likhith Bhanu
Project Type : Academic Cybersecurity Project or Tool
