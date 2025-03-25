import os
import subprocess

SCRIPT_CATEGORIES = {
    "Project Tracker": {
        "New Task": {"path": r"C:\atari-monk\code\scripting\script\project-tracker\new.py", "use_args": False},
        "End Task": {"path": r"C:\atari-monk\code\scripting\script\project-tracker\end.py", "use_args": False},
        "Stats": {"path": r"C:\atari-monk\code\scripting\script\project-tracker\stats.py", "use_args": True},
        "Report": {"path": r"C:\atari-monk\code\scripting\script\project-tracker\report.py", "use_args": True},
        "Sleep": {"path": r"C:\atari-monk\code\scripting\libs\time\sleep.py", "use_args": False}
    },
    "Project": {
        "New Prompt": {"path": r"C:\atari-monk\code\scripting\libs\project\prompt.py", "use_args": False},
        "Merge Files": {"path": r"C:\atari-monk\code\scripting\libs\project\merge.py", "use_args": False},
        "Tree": {"path": r"C:\atari-monk\code\scripting\libs\file_system\folder_tree.py", "use_args": True},
        "Commit Message": {"path": r"C:\atari-monk\code\scripting\libs\project\commit_msg.py", "use_args": False}
    },
    "Chrome": {
        "Open": {"path": r"C:\atari-monk\code\scripting\libs\chrome\open.py", "use_args": False},
        "Prompt": {"path": r"C:\atari-monk\code\scripting\libs\chrome\prompt.py", "use_args": False},
        "Store": {"path": r"C:\atari-monk\code\scripting\libs\chrome\save_tokens.py", "use_args": False},
    },
    "Links": {
        "New Link": {"path": r"C:\atari-monk\code\scripting\script\links\new.py", "use_args": False},
    },
    "Tool": {
        "Boot Time": {"path": r"C:\atari-monk\code\scripting\libs\time\boot_time.py", "use_args": False},
        "Print Json": {"path": r"C:\atari-monk\code\scripting\script\json\print_json.py", "use_args": True}
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

def run_script(script_path, script_args):
    if not os.path.exists(script_path):
        print(f"Error: The script '{script_path}' does not exist.")
        return

    command = ["python", script_path] + script_args
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running script: {e}")

def master_script():
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
                            script_data = SCRIPT_CATEGORIES[selected_category][script_name]
                            script_path = script_data["path"]
                            use_args_input = script_data["use_args"]
                            
                            script_args = []
                            if use_args_input:
                                script_args = input(f"Enter arguments for {script_name} (separated by spaces): ").split()
                            
                            print(f"\nRunning: {script_name} ({script_path}) with args: {script_args}")
                            run_script(script_path, script_args)
                        else:
                            print("Invalid script choice. Try again.")
                    except ValueError:
                        print("Please enter a valid number.")
            else:
                print("Invalid category choice. Try again.")
        except ValueError:
            print("Please enter a valid number.")
