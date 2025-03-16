import os
import subprocess

SCRIPTS = {
    "new_task": r"C:\atari-monk\code\scripting\script\project-tracker\new.py",
    "end_task": r"C:\atari-monk\code\scripting\script\project-tracker\end.py",
    "boot_time": r"C:\atari-monk\code\scripting\libs\time\boot_time.py",
}

def print_menu():
    print("\nAvailable Commands:")
    for i, (name, _) in enumerate(SCRIPTS.items(), start=1):
        print(f"{i}. {name}")
    print("0. Exit")

def run_script(script_path, *args):
    if not os.path.exists(script_path):
        print(f"Error: The script '{script_path}' does not exist.")
        return

    command = ["python", script_path] + list(args)

    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running script: {e}")

def master_script(args=None):
    while True:
        print_menu()
        choice = input("\nEnter a number to run a script: ")

        if choice == "0":
            print("Exiting...")
            break

        try:
            choice = int(choice)
            if 1 <= choice <= len(SCRIPTS):
                script_name = list(SCRIPTS.keys())[choice - 1]
                script_path = SCRIPTS[script_name]

                script_args = args if args else input(f"Enter arguments for {script_name} (separated by spaces): ").split()

                print(f"\nRunning: {script_name} ({script_path})")
                run_script(script_path, *script_args)
            else:
                print("Invalid choice. Try again.")
        except ValueError:
            print("Please enter a valid number.")
