import os
import string

def execute_command(command):
    if command == "hello":
        return "Hello, world!"
    elif command == "exit":
        return "Exiting..."
    elif command == "date":
        from datetime import datetime
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    elif command == "time":
        from datetime import datetime
        return datetime.now().strftime("%H:%M:%S")
    elif command == "help":
        return "Available commands: hello, exit, date, time, help, chkdir <path>"
    elif command.startswith("chkdir "):
        path = command[7:].strip()
        if os.path.isdir(path):
            return f"Directory '{path}' exists."
        else:
            return f"Directory '{path}' does not exist."
    elif command == "listdrives":
        drives = [f"{drive}:\\" for drive in string.ascii_uppercase if os.path.exists(f"{drive}:")]
        return "Available drives: " + ", ".join(drives) if drives else "No drives found."
    else:
        return f"Command '{command}' not recognized."
