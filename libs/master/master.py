import os
import subprocess

SCRIPT_CATEGORIES = {
    "Project Tracker Commands": {
        "New Task": r"C:\atari-monk\code\scripting\script\project-tracker\new.py",
        "End Task": r"C:\atari-monk\code\scripting\script\project-tracker\end.py",
        "Stats": r"C:\atari-monk\code\scripting\script\project-tracker\stats.py",
        "Report": r"C:\atari-monk\code\scripting\script\project-tracker\report.py",
    },
    "Links Commands": {
        "New Link": r"C:\atari-monk\code\scripting\script\links\new.py",
    },
    "Project": {
        "New Prompt": r"C:\atari-monk\code\scripting\libs\project\prompt.py",
        "Merge Files": r"C:\atari-monk\code\scripting\libs\project\merge.py",
        "Commit Message": r"C:\atari-monk\code\scripting\libs\project\commit_msg.py"
    },
    "Utility Commands": {
        "Boot Time": r"C:\atari-monk\code\scripting\libs\time\boot_time.py",
        "Print Json": r"C:\atari-monk\code\scripting\script\json\print_json.py"
    }
}

def print_main_menu():
    print("\nAvailable Categories:")
    for i, category in enumerate(SCRIPT_CATEGORIES.keys(), start=1):
        print(f"{i}. {category}")
    print("0. Exit")

def print_sub_menu(category):
    print(f"\nAvailable Scripts in {category}:")
    scripts = list(SCRIPT_CATEGORIES[category].keys())
    for i, script_name in enumerate(scripts, start=1):
        print(f"{i}. {script_name}")
    print("0. Back to Main Menu")
    return scripts

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
        print_main_menu()
        category_choice = input("\nSelect a category: ")

        if category_choice == "0":
            print("Exiting...")
            break

        try:
            category_index = int(category_choice) - 1
            categories = list(SCRIPT_CATEGORIES.keys())

            if 0 <= category_index < len(categories):
                selected_category = categories[category_index]

                while True:
                    scripts = print_sub_menu(selected_category)
                    script_choice = input("\nSelect a script to run: ")

                    if script_choice == "0":
                        break

                    try:
                        script_index = int(script_choice) - 1

                        if 0 <= script_index < len(scripts):
                            script_name = scripts[script_index]
                            script_path = SCRIPT_CATEGORIES[selected_category][script_name]

                            script_args = args if args else input(f"Enter arguments for {script_name} (separated by spaces): ").split()

                            print(f"\nRunning: {script_name} ({script_path}) with args: {script_args}")
                            run_script(script_path, *script_args)
                        else:
                            print("Invalid script choice. Try again.")
                    except ValueError:
                        print("Please enter a valid number.")

            else:
                print("Invalid category choice. Try again.")
        except ValueError:
            print("Please enter a valid number.")
