import os

# ANSI colors for CLI output
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RESET = '\033[0m'

def print_success(msg):
    print(f"{Colors.GREEN}{msg}{Colors.RESET}")

def print_error(msg):
    print(f"{Colors.RED}{msg}{Colors.RESET}")

def print_warning(msg):
    print(f"{Colors.YELLOW}{msg}{Colors.RESET}")

def save_results(filename, content):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(content + "\n")
