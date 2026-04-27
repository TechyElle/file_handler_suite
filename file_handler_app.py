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
