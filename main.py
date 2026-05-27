from logger import KeyLogger

def main():
    keylogger = KeyLogger()

    while True:
        print("\n=== CYBER KEYLOGGER MENU ===")
        print("1. Start Logging")
        print("2. Stop Logging")
        print("3. Analyzer")
        print("4. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            keylogger.start_logging()

        elif choice == "2":
            keylogger.stop_logging()

        elif choice == "4":
            keylogger.stop_logging()
            print("Exiting...")
            break

        elif choice == "3":
            import analyzer
            analyzer.analyze_logs()

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
