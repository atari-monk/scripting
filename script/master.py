import sys
sys.path.append('C:\\atari-monk\\code\\scripting')
from libs.shared import get_script_info
from libs.master import master_script

def main():
    args, _, _ = get_script_info(sys.argv)

    master_script(args)
    input("Enter to close")

if __name__ == "__main__":
    main()
