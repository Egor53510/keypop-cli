GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

def success(msg): print(f"{GREEN}✓  {msg}{RESET}")
def error(msg): print(f"{RED}✗ {msg}{RESET}")