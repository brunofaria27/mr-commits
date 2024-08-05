import os
import subprocess
import random
import datetime

def run_command(command):
    """Run a shell command and return the output."""
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error running command: {command}")
        print(result.stderr)
        exit(1)
    return result.stdout.strip()

def modify_file(file_path):
    """Modify the file by adding a comment line with a timestamp."""
    with open(file_path, 'a') as file:
        file.write(f"# Update made on {datetime.datetime.now()}\n")

def main():
    file_path = 'changes.txt'

    if not os.path.isfile(file_path):
        print(f"File {file_path} does not exist.")
        exit(1)

    modify_file(file_path)
    run_command(f'git add {file_path}')
    commit_message = f"Automated commit {datetime.datetime.now()}"
    run_command(f'git commit -m "{commit_message}"')
    run_command('git push')

if __name__ == '__main__':
    main()
