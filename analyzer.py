import os
import pandas as pd
import matplotlib.pyplot as plt

def analyze_logs():
    log_folder = "logs"

    if not os.path.exists(log_folder):
        print("No logs found.")
        return
        
    logs = []
    
    for file in os.listdir(log_folder):
        if file.endswith(".txt"):
            path = os.path.join(log_folder, file)
            with open(path, "r", encoding="utf-8") as f:
                lines = f.readlines()
                for line in lines:
                    try:
                        time, key = line.split(" - ")
                        logs.append([time, key.strip()])
                    except:
                        pass

    df = pd.DataFrame(logs, columns=["timestamp", "key"])
    if df.empty:
        print("No logs to analyze.")
        return

    print("\n=== BASIC ANALYSIS ===")
    print("Total keys pressed:", len(df))

    # top 10 most pressed keys
    print("\nTop keys:")
    print(df["key"].value_counts().head(10))

    # Graph: frequency of first 20 keys
    df["key"].value_counts().head(20).plot(kind="bar")
    plt.title("Top 20 Most Pressed Keys")
    plt.xlabel("Keys")
    plt.ylabel("Frequency")
    plt.show()

    print("\n=== SUSPICIOUS ACTIVITY REPORT ===")

    # Suspicious: too many backspaces
    backspaces = df[df["key"] == "Key.backspace"]
    print("Backspace presses:", len(backspaces))
    if len(backspaces) > 20:
        print("⚠️ ALERT: Unusual number of backspaces detected (possible password retry).")

    # Suspicious: very fast typing (<80ms)
    import datetime
    
    def to_dt(t):
        return datetime.datetime.strptime(t.split('.')[0], "%Y-%m-%d %H:%M:%S")

    df["parsed_time"] = df["timestamp"].apply(lambda x: to_dt(x))
    df["time_diff"] = df["parsed_time"].diff().dt.total_seconds()
    fast_keys = df[df["time_diff"] < 0.08]

    print("Fast typing events:", len(fast_keys))
    if len(fast_keys) > 50:
        print("⚠️ ALERT: Extremely fast typing detected (automation or high stress).")

    #CHARACTER PATTERN ANALYSIS
    print("\n=== CHARACTER PATTERN ANALYSIS ===")

    # convert dataframe keystrokes to a simple raw text string
    data = ''.join(df['key'].astype(str))

    char_count = {}
    for ch in data:
        char_count[ch] = char_count.get(ch, 0) + 1

    suspicious_patterns = []

    if char_count.get('@', 0) > 10:
        suspicious_patterns.append("Possible email typing detected (high '@' usage).")

    numbers = sum(char_count.get(n, 0) for n in "0123456789")
    if numbers > 30:
        suspicious_patterns.append("Possible OTP entry or numeric-heavy typing.")

    uppercase = sum(1 for c in data if c.isupper())
    if uppercase > 40:
        suspicious_patterns.append("Unusual uppercase typing (rage typing / emphasis).")

    for key, count in char_count.items():
        if count > 100:
            suspicious_patterns.append(f"Heavy repetition of key '{key}' ({count} presses).")

    if suspicious_patterns:
        for alert in suspicious_patterns:
            print("⚠️", alert)
    else:
        print("No suspicious character patterns found.")
        # === EXPORT REPORT TO TXT ===
    report = []

    report.append("=== KEYLOGGER ANALYSIS REPORT ===\n")
    report.append(f"Total keys pressed: {len(df)}\n")
    report.append(f"Backspace presses: {len(backspaces)}\n")
    report.append(f"Fast typing events: {len(fast_keys)}\n")

    report.append("\n--- CHARACTER PATTERN ALERTS ---\n")
    if suspicious_patterns:
        for alert in suspicious_patterns:
            report.append(f"- {alert}\n")
    else:
        report.append("No suspicious character patterns found.\n")

    report.append("\n--- TOP 10 KEYS ---\n")
    top_keys = df["key"].value_counts().head(10)
    for k, v in top_keys.items():
        report.append(f"{k}: {v}\n")

    # write to file
    os.makedirs("reports", exist_ok=True)
    filename = "reports/analysis_report.txt"

    with open(filename, "w", encoding="utf-8") as f:
        f.writelines(report)

    print(f"\nReport exported to: {filename}")



if __name__ == "__main__":
    analyze_logs()
