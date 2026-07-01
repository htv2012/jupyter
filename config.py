"""
Configuration file for ptpython.
Copy this to ~/.config/ptpython/config.py (Linux/macOS)
or %APPDATA%\ptpython\config.py (Windows).
"""

from ptpython.layout import CompletionVisualisation

__all__ = ["configure"]


def configure(repl):
    print("Configure ptpython")
    # 1. Enable Vi mode
    repl.vi_mode = True

    # 2. Do not confirm exit (Ctrl-D will exit immediately)
    repl.confirm_exit = False

    # --- Optional but highly recommended tweaks ---
    # Show line numbers
    repl.show_line_numbers = True

    # Use the native Pygments color scheme
    repl.color_depth = "DEPTH_24_BIT"  # Options: DEPTH_1_BIT, DEPTH_4_BIT, DEPTH_8_BIT, DEPTH_24_BIT
    
    # Highlight matching parentheses
    repl.show_matching_parenthesis = True

    # Completion menu visualization (POP_UP, MULTI_COLUMN, or NONE)
    repl.completion_visualisation = CompletionVisualisation.POP_UP
