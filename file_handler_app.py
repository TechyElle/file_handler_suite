"""Interactive File Handler Application.

Provides a menu-driven interface to execute all four file handling
programming exercises with an engaging user experience.
"""

import os
import sys
from typing import Dict, Callable

from file_handler_base import FileHandler
from number_separator import NumberSeparator
from student_gwa_analyzer import StudentGwaAnalyzer
from life_writer import LifeWriter
from integer_transformer import IntegerTransformer

class FileHandlerApp:
    """Main application class for the File Handler Menu System.

    Presents an interactive menu allowing users to select and run
    any of the four file handling exercises.

    Attributes:
        menu_options (Dict[str, Callable]): Mapping of menu choices
            to their corresponding handler methods.
        is_running (bool): Controls the main application loop.
    """

    def __init__(self) -> None:
        """Initialize the application with menu options."""
        self.is_running = True
        self.menu_options: Dict[str, Callable[[], None]] = {
            "1": self._run_number_separator,
            "2": self._run_gwa_analyzer,
            "3": self._run_life_writer,
            "4": self._run_integer_transformer,
            "5": self._show_about,
            "0": self._exit_application,
        }
        
    def _clear_screen(self) -> None:
        """Clear the terminal screen for better readability."""
        os.system("cls" if os.name == "nt" else "clear")

    def _print_banner(self) -> None:
        """Display the application welcome banner."""
        banner = """
        ╔═══════════════════════════════════════════════════╗
        ║                                                   ║
        ║     CMPE 103 - FILE HANDLING WITH PYTHON          ║
        ║          Object-Oriented Edition                  ║
        ║                                                   ║
        ╚═══════════════════════════════════════════════════╝
        """
        print(banner)

    def _print_menu(self) -> None:
        """Display the main menu options."""
        menu = """
        ┌─────────────────────────────────────────────────┐
        │  SELECT AN ACTIVITY:                            │
        ├─────────────────────────────────────────────────┤
        │  [1] Separate Even & Odd Numbers   (P-1)        │
        │  [2] Find Top Student by GWA       (P-2)        │
        │  [3] Interactive Life Writer       (P-3)        │
        │  [4] Square Evens & Cube Odds      (P-4)        │
        ├─────────────────────────────────────────────────┤
        │  [5] About This Application                     │
        │  [0] Exit                                       │
        └─────────────────────────────────────────────────┘
        """
        print(menu)

    def _get_menu_choice(self) -> str:
        """Prompt the user for a menu selection.

        Returns:
            The user's menu choice as a string.
        """
        return input("Enter your choice: ").strip()
        
    def _execute_handler(self, handler: FileHandler) -> None:
        """Execute a file handler's process and display methods.

        Args:
            handler: An instance of a FileHandler subclass.
        """
        try:
            handler.process()
            handler.display_result()
        except Exception as error:
            print(f"\nAn error occurred: {error}\n")

    def _run_activity(
        self,
        title: str,
        description: str,
        handler_factory: Callable[[], FileHandler]
    ) -> None:
        """Generic runner for file handling activities.

        Args:
            title: Title of the activity.
            description: Brief description of source/output.
            handler_factory: Function that returns a FileHandler instance.
        """
        print(f"\n>>> Running: {title}")
        print(f"    {description}\n")

        try:
            handler = handler_factory()
            self._execute_handler(handler)
        except Exception as error:
            print(f"\nFailed to initialize or run activity: {error}\n")

        input("Press Enter to return to the menu...")
        
    def _run_number_separator(self) -> None:
        """Execute Problem P-1: Number Separation."""
        self._run_activity(
            "Number Separator (P-1)",
            "Source: numbers.txt -> even.txt & odd.txt",
            lambda: NumberSeparator("numbers.txt")
        )

    def _run_gwa_analyzer(self) -> None:
        """Execute Problem P-2: GWA Analysis."""
        self._run_activity(
            "Student GWA Analyzer (P-2)",
            "Source: students_gwa.txt",
            lambda: StudentGwaAnalyzer("students_gwa.txt")
        )

    def _run_life_writer(self) -> None:
        """Execute Problem P-3: Interactive Life Writer."""
        self._run_activity(
            "Life Writer (P-3)",
            "Output: mylife.txt",
            lambda: LifeWriter()
        )

    def _run_integer_transformer(self) -> None:
        """Execute Problem P-4: Integer Transformation."""
        self._run_activity(
            "Integer Transformer (P-4)",
            "Source: integers.txt -> double.txt & triple.txt",
            lambda: IntegerTransformer("integers.txt")
        )
