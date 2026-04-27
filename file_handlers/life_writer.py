"""Module for interactively writing lines to a text file.

Implements Problem P-3: Write multiple lines of text into mylife.txt
through an interactive prompt-based interface.
"""

from typing import List

from file_handler_base import FileHandler

class LifeWriter(FileHandler):
    """Interactively collect and write lines to mylife.txt.

    Prompts the user for multiple lines of text and writes
    all collected lines to a single output file.

    Attributes:
        collected_lines (List[str]): Lines gathered from user input.
        output_file_path (str): Path to the written output file.
    """

    def __init__(
        self,
        output_directory: str = "."
    ) -> None:
        """Initialize the LifeWriter.

        Args:
            output_directory: Directory for the output file.
        """
        super().__init__("", output_directory)
        self.collected_lines: List[str] = []
        self.output_file_path: str = ""
