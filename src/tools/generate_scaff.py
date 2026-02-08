from pathlib import Path
from .colors import colored, ORANGE, BLUE, RED, BRIGHT_YELLOW

PREFIX = "gen-"

def generate_directories():
    print(colored("Generating Default Directories:\n", RED))

    PROJ_DIR = Path(__file__).resolve().parent.parent.parent.parent

    dirs = ["data", "automation", "outputs"]

    print(f"{colored("SELECTED DIR -> ", BLUE, True)}{colored(PROJ_DIR, BRIGHT_YELLOW)}")

    for dir in dirs:
        d = PROJ_DIR/(PREFIX.upper()+(dir.capitalize()))
        d.mkdir(parents=True, exist_ok=True)
        print(colored(f"Created folder: {d}", ORANGE))

if __name__ == "__main__":
    generate_directories()