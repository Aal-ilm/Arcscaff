# colors.py
# A simple module for terminal text colors using ANSI escape codes

RESET = "\033[0m"
BOLD = "\033[1m"
UNDERLINE = "\033[4m"

# Standard colors
BLACK = "\033[30m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"

# Bright colors
BRIGHT_BLACK = "\033[90m"
BRIGHT_RED = "\033[91m"
BRIGHT_GREEN = "\033[92m"
BRIGHT_YELLOW = "\033[93m"
BRIGHT_BLUE = "\033[94m"
BRIGHT_MAGENTA = "\033[95m"
BRIGHT_CYAN = "\033[96m"
BRIGHT_WHITE = "\033[97m"

# Extended 256-color codes
ORANGE = "\033[38;5;208m"   # bright orange
PURPLE = "\033[38;5;93m"    # soft purple
LIGHT_BLUE = "\033[38;5;81m"
PINK = "\033[38;5;213m"
TEAL = "\033[38;5;37m"

# Helper functions
def colored(text: str, color: str, bold: bool = False) -> str:
    """
    Return text string wrapped in ANSI color codes.
    
    Args:
        text: Text to color
        color: Color code string from above
        bold: If True, make text bold
    
    Returns:
        Colored text string
    """
    style = BOLD if bold else ""
    return f"{style}{color}{text}{RESET}"
