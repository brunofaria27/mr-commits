import os
import subprocess
import random
import datetime

def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error running command: {command}")
        print(result.stderr)
        exit(1)
    return result.stdout.strip()

def modify_file(file_path):
    with open(file_path, 'a') as file:
        file.write(f"# Update made on {datetime.datetime.now()}\n")

def run(file_path):
    modify_file(file_path)
    run_command(f'git add {file_path}')
    commit_message = f"Automated commit {datetime.datetime.now()}"
    run_command(f'git commit -m "{commit_message}"')
    run_command('git push')

def main():
    file_path = 'changes.txt'

    if not os.path.isfile(file_path):
        print(f"File {file_path} does not exist.")
        exit(1)

    for _ in range(0, 10000):
        run(file_path)

if __name__ == '__main__':
    main()
